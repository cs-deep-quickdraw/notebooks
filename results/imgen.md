# Description

Models trained by generating the images from the strokes

# Results

## 64x64 Images

### Pretrained mobilenet 12k per class

Config:
```python
# Config:
batch_size = 256
learning_rate = 0.001

img_size = 64
train_classes = classes[:]


N_train = 12000
N_val = N_train // 5
# N_test = N_val
N_test = 0
N_test_reserved = 20000

n_epochs = 10
```

Results:

```
Epoch: 1/10, loss: 0.7174502165269729, validation accuracy: 84.28583333333333% took: 509.21234345436096 seconds
Epoch: 2/10, loss: 0.5585970539574229, validation accuracy: 86.11083333333333% took: 509.7822926044464 seconds
Epoch: 3/10, loss: 0.509766736109153, validation accuracy: 86.6775% took: 510.26687264442444 seconds
Epoch: 4/10, loss: 0.4794071838005411, validation accuracy: 87.03416666666666% took: 515.2203142642975 seconds
Epoch: 5/10, loss: 0.45612751672508467, validation accuracy: 87.41625% took: 508.9523000717163 seconds
Epoch: 6/10, loss: 0.4380846023495999, validation accuracy: 87.62833333333333% took: 506.36477851867676 seconds
Epoch: 7/10, loss: 0.42134666496906875, validation accuracy: 87.99833333333333% took: 508.7484474182129 seconds
Epoch: 8/10, loss: 0.4074481981409135, validation accuracy: 87.99333333333334% took: 505.14482402801514 seconds
Epoch: 9/10, loss: 0.39537988634900834, validation accuracy: 87.99416666666667% took: 498.74235486984253 seconds
Epoch: 10/10, loss: 0.38354334374412946, validation accuracy: 88.17833333333333% took: 498.92996621131897 seconds
Training ended after 10 ! Best validation accuracy: 88.17833333333333%
```

### Pretrained mobilenet 34k per class

Results:
```
Epoch: 1/10, loss: 0.5553819374581199, validation accuracy: 87.71558823529412% took: 12868.160160541534 seconds
Epoch: 2/10, loss: 0.4477839009686326, validation accuracy: 88.96764705882353% took: 12878.031504154205 seconds
Epoch: 3/10, loss: 0.4164512191808278, validation accuracy: 89.24573529411765% took: 12815.621380090714 seconds
Epoch: 4/10, loss: 0.3973323991253977, validation accuracy: 89.69235294117647% took: 12831.34978890419 seconds
Epoch: 5/10, loss: 0.3831660436787564, validation accuracy: 89.87838235294117% took: 12845.545823812485 seconds
Epoch: 6/10, loss: 0.3722130690321561, validation accuracy: 90.08808823529412% took: 12859.492151021957 seconds
batch: 19172, current loss: 0.3624596437682209=>> PBS: job killed: walltime 86489 exceeded limit 86400
```

### Pretrained resnet 3k per class

Config:
```python
# Config:
batch_size = 256
learning_rate = 0.001

img_size = 64
train_classes = classes[:]

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

### Pretrained resnet 12k per class

Config:
```python
# Config:
batch_size = 256
learning_rate = 0.001

img_size = 64
train_classes = classes[:]

preprocessor = resnet_preprocess
N_train = 12000
N_val = N_train // 5
# N_test = N_val
N_test = 0
N_test_reserved = 20000

n_epochs = 10
```

Results:
```
Epoch: 1/10, loss: 0.6774668015933789, validation accuracy: 85.07416666666667% took: 491.9338881969452 seconds
Epoch: 2/10, loss: 0.5094687837452561, validation accuracy: 86.69875% took: 487.3147134780884 seconds
Epoch: 3/10, loss: 0.4399917041437872, validation accuracy: 87.21833333333333% took: 485.8715076446533 seconds
Epoch: 4/10, loss: 0.38498844693926615, validation accuracy: 87.52208333333333% took: 489.63020968437195 seconds
Epoch: 5/10, loss: 0.3343800108835305, validation accuracy: 87.63583333333334% took: 487.9115149974823 seconds
Epoch: 6/10, loss: 0.2875199774836441, validation accuracy: 87.54458333333334% took: 484.3381268978119 seconds
Epoch: 7/10, loss: 0.24652182898220348, validation accuracy: 87.49083333333333% took: 485.0930242538452 seconds
Epoch: 8/10, loss: 0.21162572076366165, validation accuracy: 87.25791666666667% took: 487.8054440021515 seconds
Epoch: 9/10, loss: 0.18296313381502755, validation accuracy: 87.09958333333333% took: 479.86763405799866 seconds
Epoch: 10/10, loss: 0.16095749204088347, validation accuracy: 86.95291666666667% took: 476.1966917514801 seconds
Training ended after 10 ! Best validation accuracy: 87.63583333333334%
```

### Pretrained resnet 34k per class

Results:
```
Epoch: 1/15, loss: 0.5753659192983724, validation accuracy: 87.15985294117647% took: 1512.9524774551392 seconds
Epoch: 2/15, loss: 0.44130522037841274, validation accuracy: 88.4885294117647% took: 1518.2521574497223 seconds
Epoch: 3/15, loss: 0.3908435369095266, validation accuracy: 88.90544117647059% took: 1517.0163519382477 seconds
Epoch: 4/15, loss: 0.3525028056311528, validation accuracy: 88.97161764705882% took: 1518.7357697486877 seconds
Epoch: 5/15, loss: 0.31745304685535336, validation accuracy: 89.21602941176471% took: 1517.490399837494 seconds
Epoch: 6/15, loss: 0.2843009522545142, validation accuracy: 89.03735294117647% took: 1514.675742149353 seconds
Epoch: 7/15, loss: 0.2535711930566318, validation accuracy: 89.02838235294118% took: 1514.9144098758698 seconds
Epoch: 8/15, loss: 0.22533909949949305, validation accuracy: 88.88941176470588% took: 1515.028909444809 seconds
Epoch: 9/15, loss: 0.20110118082456516, validation accuracy: 88.70132352941177% took: 1515.2387645244598 seconds
Epoch: 10/15, loss: 0.18063540006062878, validation accuracy: 88.51794117647059% took: 1515.2414858341217 seconds
Epoch: 11/15, loss: 0.16378694288112855, validation accuracy: 88.505% took: 1516.1395182609558 seconds
Epoch: 12/15, loss: 0.14962784641703789, validation accuracy: 88.38382352941177% took: 1515.1115653514862 seconds
Epoch: 13/15, loss: 0.13731823968684936, validation accuracy: 88.2885294117647% took: 1517.806363105774 seconds
batch: 6690, current loss: 0.11876187290083089
Epoch: 14/15, loss: 0.12689112933562105, validation accuracy: 88.27588235294118% took: 1518.3629105091095 seconds
Epoch: 15/15, loss: 0.11781168516129008, validation accuracy: 88.20117647058824% took: 1517.6389863491058 seconds
Training ended after 15 ! Best validation accuracy: 89.21602941176471%
```

## 96x96 Images

### Pretrained resnet 34k per class

Results:
```
Epoch: 1/15, loss: 0.5315123028820976, validation accuracy: 87.92191176470588% took: 2259.5629444122314 seconds
Epoch: 2/15, loss: 0.4104623845613626, validation accuracy: 88.9975% took: 2258.257215499878 seconds
Epoch: 3/15, loss: 0.3611152861040142, validation accuracy: 89.47514705882352% took: 2259.9859058856964 seconds
Epoch: 4/15, loss: 0.32156519729858907, validation accuracy: 89.57485294117647% took: 2258.6150007247925 seconds
Epoch: 5/15, loss: 0.28417278116406525, validation accuracy: 89.55426470588235% took: 2255.5964698791504 seconds
Epoch: 6/15, loss: 0.24883482988798694, validation accuracy: 89.50411764705882% took: 2255.6814489364624 seconds
Epoch: 7/15, loss: 0.21686368812750106, validation accuracy: 89.30529411764707% took: 2257.1828796863556 seconds
Epoch: 8/15, loss: 0.18945416671367962, validation accuracy: 89.19632352941177% took: 2253.6237778663635 seconds
Epoch: 9/15, loss: 0.16696215126432895, validation accuracy: 89.09779411764706% took: 2259.2301466464996 seconds
Epoch: 10/15, loss: 0.14834158650172113, validation accuracy: 88.91470588235295% took: 2258.2714710235596 seconds
Epoch: 11/15, loss: 0.13308760571084438, validation accuracy: 88.88558823529412% took: 2253.561711549759 seconds
Epoch: 12/15, loss: 0.12062631426509506, validation accuracy: 88.67941176470588% took: 2252.9999198913574 seconds
Epoch: 13/15, loss: 0.10981412574538349, validation accuracy: 88.72808823529412% took: 2258.6549179553986 seconds
Epoch: 14/15, loss: 0.10049851115366945, validation accuracy: 88.72323529411764% took: 2248.5140697956085 seconds
Epoch: 15/15, loss: 0.09259502314169399, validation accuracy: 88.59691176470588% took: 2253.4305210113525 seconds
Training ended after 15 ! Best validation accuracy: 89.57485294117647%
```
