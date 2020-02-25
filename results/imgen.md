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
