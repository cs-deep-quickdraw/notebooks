# -*- coding: utf-8 -*-
"""quickdraw_lstm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OdaFtDjz7n4kkalv95f_CoVVLrST1qtt
"""

import struct
from struct import unpack
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(42)
np.random.seed(42)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('device = {}'.format(device))

# Helper from: https://github.com/googlecreativelab/quickdraw-dataset/blob/master/examples/binary_file_parser.py
def unpack_drawing(file_handle):
    # Skip key_id: 8, countrycode: 2, recognized: 1, timestamp: 4 = 15
    file_handle.read(15)
    n_strokes, = unpack('H', file_handle.read(2))
    idx = 0

    N = 0
    strokes = []
    for i in range(n_strokes):
      n_points, = unpack('H', file_handle.read(2))
      N += n_points
      fmt = str(n_points) + 'B'
      x = unpack(fmt, file_handle.read(n_points))
      y = unpack(fmt, file_handle.read(n_points))
      strokes.append((x, y))

    image = np.zeros((N, 3), dtype=np.float32)


    # Return a tensor of size number of stroke x 3 like here: https://github.com/tensorflow/docs/blob/master/site/en/r1/tutorials/sequences/recurrent_quickdraw.md#optional-converting-the-data
    for i, (x, y) in enumerate(strokes):
        n_points = len(x)
        image[idx:idx+n_points, 0] = np.asarray(x)
        image[idx:idx+n_points, 1] = np.asarray(y)
        idx += n_points
        # Mark stroke end with a 1
        image[idx -1, 2] = 1


    # Preprocessing.
    # 1. Size normalization.
    lower = np.min(image[:, 0:2], axis=0)
    upper = np.max(image[:, 0:2], axis=0)
    scale = upper - lower
    scale[scale == 0] = 1
    image[:, 0:2] = (image[:, 0:2] - lower) / scale
    # 2. Compute deltas.
    image[1:, 0:2] -= image[0:-1, 0:2]
    image = image[1:, :]

    return torch.FloatTensor(image)


def unpack_drawings(filename):
    with open(filename, 'rb') as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break

import urllib.request
from pathlib import Path

urllib.request.urlretrieve('https://raw.githubusercontent.com/cs-deep-quickdraw/notebooks/master/100_classes.txt', '100_classes.txt')

# Create data dir
Path("./data").mkdir(exist_ok=True)

f = open("100_classes.txt","r")
# And for reading use
classes = [cls.strip() for cls in f.readlines()]
f.close()

def download(classes):
  base = 'https://storage.googleapis.com/quickdraw_dataset/full/binary/'
  for i, c in enumerate(classes):
    cls_url = c.replace('_', '%20')
    path = base+cls_url+'.bin'
    print((1+i)/len(classes), c, path)
    urllib.request.urlretrieve(path, 'data/'+c+'.bin')

download(classes)

i_drawings = unpack_drawings("data/anvil.bin")

from pprint import pprint
pprint(next(i_drawings)[:2])
pprint(next(i_drawings)[:2])

class StrokeClassifier(nn.Module):

  def __init__(self, cv1, hidden_dim, n_layers, n_classes, bidirectional):
    super(StrokeClassifier, self).__init__()
    self.hidden_dim = hidden_dim

    input_size = 3

    self.bn = nn.BatchNorm1d(input_size)
    self.conv1 = nn.Conv1d(input_size, cv1[0], cv1[1])
    
    # The LSTM takes 3 things as input (x, y, isLastPoint) and outputs hidden states with dimensionality hidden_dim
    self.lstm = nn.LSTM(cv1[0], hidden_dim, n_layers, batch_first=True, bidirectional=bidirectional)

    # The linear layer maps the LSTM output to a linear space
    self.linear = nn.Linear(hidden_dim * 2 if bidirectional else hidden_dim, n_classes)

  def forward(self, strokes):
    # BN and Convolution expect NCWH
    strokes = self.bn(strokes)
    strokes = self.conv1(strokes)

    # LSTM expect NHWC
    strokes = torch.transpose(strokes, 1, 2)
    out, _ = self.lstm(strokes)

    # Keep last layer of the NN
    out = out[:,-1,:]
    out = self.linear(out)
    return out

from torch.utils.data import Dataset

class DrawDataset(Dataset):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        assert len(self.X) == len(self.Y)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        return [torch.Tensor(self.X[idx]).type('torch.FloatTensor'), self.Y[idx]]

# Config:
batch_size = 256
learning_rate = 0.001

hidden_size = 64
n_layers = 2
train_classes = classes[:]
conv1 = (128, 5)
bidirectional = True

N_train = 60000
N_val = 8000
N_test = 10000
N_test_reserved = 20000
max_padding = 100
n_epochs = 20

from itertools import islice
from torch.nn.utils.rnn import pad_sequence

def extract_dataset(samples_train, samples_val, samples_test, test_reserved, classes, max_padding=100):
  X_train = []
  X_val = []
  X_test = []
  y_train = []
  y_val = []
  y_test = []

  for c, cls in enumerate(classes):
    drawings = unpack_drawings('data/' + cls + '.bin')

    # TODO: better way of doing this
    for _ in range(samples_train):
      X_train.append(next(drawings))
      y_train.append(c)

    # TODO: itertools
    for _ in range(max(0, test_reserved - samples_train)):
      next(drawings)

    for _ in range(samples_val):
      X_val.append(next(drawings))
      y_val.append(c)

    for _ in range(samples_test):
      X_test.append(next(drawings))
      y_test.append(c)
  
    if c % 10 == 0:
      print(f"done extracting class: {cls}: {1 + c} / {len(classes)}")
    

  def norm(X):
    return torch.transpose(pad_sequence(X, batch_first=True)[:, :max_padding, :], 1, 2)

  # XXX: instead of padding like that we could have a moving window:
  # Example if we want 100 sequences and we have an image with 200 we can use the windows:
  # 0-100, 10-110, ... 100-200 for instance, this would add data
  X_train = norm(X_train)
  X_val = norm(X_val)
  X_test = norm(X_test)
  print("training shape", X_train.shape)
  print("validation shape", X_val.shape)
  print("testing shape", X_test.shape)
  print("classes", len(classes))

  return DrawDataset(X_train, y_train), DrawDataset(X_val, y_val), DrawDataset(X_test, y_test)

def evaluate_model(model, loader):
  with torch.no_grad():
    correct = 0
    total = 0
    
    for i, (img, label) in enumerate(loader):
      img = img.to(device)
      label = label.to(device)

      out = model(img)

      _, pred = torch.max(out.data, 1)

      total += label.size(0)
      correct += (pred == label).sum().item()

    return 100. * correct / total


import copy
import time

def train_model(model, opt, loss_fn, loader, v_loader, n_epochs):

  best_acc, best_model = 0, None
  losses, accs = [], []
  for epoch in range(n_epochs):
    start = time.time()
    epoch_losses = []
    for i, (img, lab) in enumerate(loader):
      print(f"\rbatch: {i}, current loss: {np.mean(epoch_losses) if epoch_losses else 'NaN'}", end='')
      img = img.to(device)
      lab = torch.LongTensor(lab).to(device)

      out = model(img)

      loss = loss_fn(out, lab)

      opt.zero_grad()
      loss.backward()
      opt.step()

      epoch_losses.append(loss.item())

    print("\rEvaluating model on validation dataset...", end='')
    val_acc = evaluate_model(model, v_loader)
    mean_loss = np.mean(epoch_losses)

    losses.append(mean_loss)
    accs.append(val_acc)

    if val_acc > best_acc:
      best_acc = val_acc
      best_model = copy.deepcopy(model.state_dict())

    print(f"\rEpoch: {epoch+1}/{n_epochs}, loss: {mean_loss}, validation accuracy: {val_acc}% took: {time.time() - start} seconds")

  print(f"Training ended after {n_epochs} ! Best validation accuracy: {best_acc}%")
  return best_model, losses, accs

from torch.nn.utils.rnn import pad_sequence

# TODO: really take the last 2k images for testing
train_dataset, val_dataset, test_dataset = extract_dataset(N_train, N_val, N_test, N_test_reserved, train_classes, max_padding=max_padding)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
val_loader = torch.utils.data.DataLoader(dataset=val_dataset, batch_size=batch_size, shuffle=False)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

import torch.optim as optim

model = StrokeClassifier(conv1, hidden_size, n_layers, len(train_classes), bidirectional).to(device)
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr = learning_rate)
# optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

best_model, losses, accs = train_model(model, optimizer, loss_function, train_loader, val_loader, n_epochs)

print(f"Test accuracy: {evaluate_model(best_model, test_loader)}%")

import time

model_path = f'lstm_quickdraw.model.{time.time()}'
torch.save(model, model_path)

print(f"Model saved at: {model_path}")
