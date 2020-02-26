# Description

Models trained by generating the images from the strokes

# Results

## 64x64 Images

### Pretrained mobilenet 8k per class

Config:
```python
# Config:
batch_size = 256
learning_rate = 0.001

img_size = 64
train_classes = classes[:]


N_train = 8000
N_val = N_train // 5
# N_test = N_val
N_test = 0
N_test_reserved = 20000

n_epochs = 5
```

Results:

```
Epoch: 1/5, loss: 0.7777804596445768, validation accuracy: 79.18075% took: 3607.68372511863708 seconds
Epoch: 2/5, loss: 0.6005541498565674, validation accuracy: 84.67375% took: 3607.0781791210175 seconds
Epoch: 3/5, loss: 0.5505085116481782, validation accuracy: 85.44875% took: 3606.7783970832825 seconds
Epoch: 4/5, loss: 0.5162633287239075, validation accuracy: 85.85625% took: 3621.3950605392456 seconds
Epoch: 5/5, loss: 0.4910012597179413, validation accuracy: 86.186875% took: 3634.4329283237457 seconds
```

### Pretrained resnet 3k per class

Config:
```python
# Config:
batch_size = 256
learning_rate = 0.001

img_size = 64
train_classes = classes[:]

preprocessor = resnet_preprocess
N_train = 3000
N_val = N_train // 5
# N_test = N_val
N_test = 0
N_test_reserved = 20000

n_epochs = 10
```

Results:
```
Epoch: 1/10, loss: 0.8692755306031517, validation accuracy: 81.6% took: 186.59947395324707 seconds
Epoch: 2/10, loss: 0.6052859179904436, validation accuracy: 82.78333333333333% took: 186.03426814079285 seconds
Epoch: 3/10, loss: 0.5100248240621017, validation accuracy: 83.85% took: 186.34885048866272 seconds
Epoch: 4/10, loss: 0.43686941946275, validation accuracy: 84.075% took: 187.46090126037598 seconds
Epoch: 5/10, loss: 0.3705878897535109, validation accuracy: 84.295% took: 186.95994186401367 seconds
Epoch: 6/10, loss: 0.31145934840670625, validation accuracy: 84.36666666666666% took: 186.71059131622314 seconds
Epoch: 7/10, loss: 0.260530869784819, validation accuracy: 84.22833333333334% took: 187.1522433757782 seconds
Epoch: 8/10, loss: 0.21728751901219323, validation accuracy: 83.86833333333334% took: 186.16959762573242 seconds
Epoch: 9/10, loss: 0.18256917312970136, validation accuracy: 83.89% took: 188.39868021011353 seconds
Epoch: 10/10, loss: 0.15756501417619784, validation accuracy: 83.83333333333333% took: 187.49724078178406 seconds
Training ended after 10 ! Best validation accuracy: 84.36666666666666%
```
