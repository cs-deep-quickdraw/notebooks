# Description

models can be found under the `lstm` directory as pytorch `state_dict`'s, the convention for their name is:

`<type>_lay<n_lstm_layers>_sz<lstm_hidden_size>.model` for non convolutional models

and

`<type>_cv1<conv1_params>_lay<n_lstm_layers>_sz<lstm_hidden_size>.model`

or

`<type>_cv1<conv1_params>_cv2<conv2_params>_lay<n_lstm_layers>_sz<lstm_hidden_size>.model`

for models with convolution layers.

# Results

## Simple LSTM

### 1 layer

#### Size 64

Config:
```python
batch_size = 256
learning_rate = 0.001

hidden_size = 64
n_layers = 1
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = None # (128, 5)
conv2 = None
bidirectional = False

N_train = 20000
N_val = N_train // 5
N_test = N_val
N_test_reserved = 20000
max_padding = 100
n_epochs = 10
```

Results:

```
Epoch: 1/10, loss: 3.7877804596445768, validation accuracy: 12.18075% took: 85.73434066772461 seconds
Epoch: 2/10, loss: 2.7548682960340343, validation accuracy: 23.64475% took: 84.91592526435852 seconds
Epoch: 3/10, loss: 2.0737051215563023, validation accuracy: 34.68525% took: 85.68372511863708 seconds
Epoch: 4/10, loss: 1.7293755938572568, validation accuracy: 41.48675% took: 85.85774946212769 seconds
Epoch: 5/10, loss: 1.53600292222289, validation accuracy: 45.4705% took: 85.85911870002747 seconds
Epoch: 6/10, loss: 1.4183073640251136, validation accuracy: 49.37025% took: 85.58963251113892 seconds
Epoch: 7/10, loss: 1.3346304411880798, validation accuracy: 51.46275% took: 86.11428451538086 seconds
Epoch: 8/10, loss: 1.2747747892227548, validation accuracy: 51.846% took: 85.57981395721436 seconds
Epoch: 9/10, loss: 1.2305504589201042, validation accuracy: 54.52425% took: 85.80500364303589 seconds
Epoch: 10/10, loss: 1.1950125450607636, validation accuracy: 55.08175% took: 85.68330955505371 seconds
Training ended after 10 ! Best validation accuracy: 55.08175%
```

#### Size 256

Config:

```python
# Config:
batch_size = 256
learning_rate = 0.001

hidden_size = 256
n_layers = 1
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = None # (128, 5)
conv2 = None
bidirectional = False

N_train = 20000
N_val = N_train // 5
N_test = N_val
N_test_reserved = 20000
max_padding = 100
n_epochs = 10
```

Results:
```
Epoch: 1/10, loss: 2.783527677432685, validation accuracy: 54.7115% took: 153.96742296218872 seconds
Epoch: 2/10, loss: 0.9768686812710978, validation accuracy: 67.10025% took: 153.85839748382568 seconds
Epoch: 3/10, loss: 0.7582797594554412, validation accuracy: 72.373% took: 154.46974325180054 seconds
Epoch: 4/10, loss: 0.6668542796047613, validation accuracy: 75.6255% took: 154.2045316696167 seconds
Epoch: 5/10, loss: 0.6150482786185424, validation accuracy: 76.8065% took: 154.68227529525757 seconds
Epoch: 6/10, loss: 0.5801469895730751, validation accuracy: 77.51375% took: 154.3025188446045 seconds
Epoch: 7/10, loss: 0.5543020138030441, validation accuracy: 78.241% took: 154.91842246055603 seconds
Epoch: 8/10, loss: 0.5347797621704774, validation accuracy: 79.14625% took: 153.85254073143005 seconds
Epoch: 9/10, loss: 0.5192326117298842, validation accuracy: 79.66825% took: 153.9149079322815 seconds
Epoch: 10/10, loss: 0.5061628646861571, validation accuracy: 79.7425% took: 154.259685754776 seconds
Training ended after 10 ! Best validation accuracy: 79.7425%
```


### 2 layers

#### Size 64


Config:

```python
# Config:
batch_size = 256
learning_rate = 0.001

hidden_size = 64
n_layers = 2
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = None # (128, 5)
conv2 = None
bidirectional = False

N_train = 20000
N_val = N_train // 5
N_test = N_val
N_test_reserved = 20000
max_padding = 100
n_epochs = 10
```

Results:

```
Epoch: 1/10, loss: 3.883484064991032, validation accuracy: 20.3395% took: 119.14738178253174 seconds
Epoch: 2/10, loss: 1.9121948401723188, validation accuracy: 49.086% took: 120.39017486572266 seconds
Epoch: 3/10, loss: 1.2383372679755185, validation accuracy: 59.277% took: 120.01821184158325 seconds
Epoch: 4/10, loss: 1.0306251169807334, validation accuracy: 64.2195% took: 120.38624572753906 seconds
Epoch: 5/10, loss: 0.927735268795031, validation accuracy: 66.275% took: 121.06590843200684 seconds
Epoch: 6/10, loss: 0.8641707723857529, validation accuracy: 67.5375% took: 120.61723852157593 seconds
Epoch: 7/10, loss: 0.8205510407598501, validation accuracy: 69.3185% took: 120.4512550830841 seconds
Epoch: 8/10, loss: 0.7887364783772857, validation accuracy: 70.0575% took: 120.77535367012024 seconds
Epoch: 9/10, loss: 0.7643155072961499, validation accuracy: 71.44175% took: 121.33180928230286 seconds
Epoch: 10/10, loss: 0.7451926151906332, validation accuracy: 72.003% took: 121.2354621887207 seconds
Training ended after 10 ! Best validation accuracy: 72.003%
```

#### Size 128

Config:

```python
# Config:
batch_size = 128
learning_rate = 0.001

hidden_size = 256
n_layers = 2
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = None # (128, 5)
conv2 = None
bidirectional = False

N_train = 20000
N_val = N_train // 5
N_test = N_val
N_test_reserved = 20000
max_padding = 100
n_epochs = 10
```

Results:

```
Epoch: 1/10, loss: 2.302578472357225, validation accuracy: 59.1915% took: 135.34909796714783 seconds
Epoch: 2/10, loss: 0.8924322406216955, validation accuracy: 71.204% took: 134.3272476196289 seconds
Epoch: 3/10, loss: 0.712666801212845, validation accuracy: 75.45875% took: 134.3958899974823 seconds
Epoch: 4/10, loss: 0.6359579696608585, validation accuracy: 77.20875% took: 135.057941198349 seconds
Epoch: 5/10, loss: 0.5918515812537436, validation accuracy: 78.248% took: 135.2409632205963 seconds
Epoch: 6/10, loss: 0.5622468224854044, validation accuracy: 79.074% took: 134.95159888267517 seconds
Epoch: 7/10, loss: 0.5406473592204076, validation accuracy: 79.32075% took: 135.09947776794434 seconds
Epoch: 8/10, loss: 0.52400127871461, validation accuracy: 80.48425% took: 135.2522828578949 seconds
Epoch: 9/10, loss: 0.5108651428285671, validation accuracy: 81.149% took: 134.45793843269348 seconds
Epoch: 10/10, loss: 0.4996846826520815, validation accuracy: 80.89525% took: 134.71141815185547 seconds
Training ended after 10 ! Best validation accuracy: 81.149%
```

#### Size 256

Config:

```python
# Config:
batch_size = 256
learning_rate = 0.001

hidden_size = 256
n_layers = 2
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = None # (128, 5)
conv2 = None
bidirectional = False

N_train = 20000
N_val = N_train // 5
N_test = N_val
N_test_reserved = 20000
max_padding = 100
n_epochs = 10
```

Results:

```
Epoch: 1/10, loss: 2.3433144869258764, validation accuracy: 66.62025% took: 257.9390285015106 seconds
Epoch: 2/10, loss: 0.7326909650475241, validation accuracy: 76.37075% took: 257.95626187324524 seconds
Epoch: 3/10, loss: 0.5769127620429155, validation accuracy: 79.9755% took: 258.97781205177307 seconds
Epoch: 4/10, loss: 0.5113018184659973, validation accuracy: 81.48125% took: 258.3016881942749 seconds
Epoch: 5/10, loss: 0.47145766145316675, validation accuracy: 82.402% took: 257.3997220993042 seconds
Epoch: 6/10, loss: 0.44298887378303126, validation accuracy: 82.50325% took: 257.0086762905121 seconds
Epoch: 7/10, loss: 0.4202901058544595, validation accuracy: 83.031% took: 255.39920139312744 seconds
Epoch: 8/10, loss: 0.4014823855392365, validation accuracy: 83.14125% took: 257.74062037467957 seconds
Epoch: 9/10, loss: 0.38538270862600216, validation accuracy: 83.3% took: 258.16210174560547 seconds
Epoch: 10/10, loss: 0.37134333474412096, validation accuracy: 83.49% took: 259.6124622821808 seconds
Training ended after 10 ! Best validation accuracy: 83.49%
```

## BiLSTM

### 1 layer

#### Size 64

Config:

```python
# Config:
batch_size = 256
learning_rate = 0.001

hidden_size = 64
n_layers = 1
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = None # (128, 5)
conv2 = None
bidirectional = True

N_train = 20000
N_val = N_train // 5
N_test = N_val
N_test_reserved = 20000
max_padding = 100
n_epochs = 10
```

Results:

```
Epoch: 1/10, loss: 3.750726910295368, validation accuracy: 17.57625% took: 120.00426959991455 seconds
Epoch: 2/10, loss: 2.3574404854269746, validation accuracy: 30.25825% took: 121.44381976127625 seconds
Epoch: 3/10, loss: 1.693413782955879, validation accuracy: 40.00475% took: 121.1829206943512 seconds
Epoch: 4/10, loss: 1.4552458309416245, validation accuracy: 45.6085% took: 121.54740023612976 seconds
Epoch: 5/10, loss: 1.3393976971188566, validation accuracy: 48.1245% took: 121.05478978157043 seconds
Epoch: 6/10, loss: 1.264559272277619, validation accuracy: 49.8545% took: 121.7063364982605 seconds
Epoch: 7/10, loss: 1.2118903881957586, validation accuracy: 51.248% took: 121.09454131126404 seconds
Epoch: 8/10, loss: 1.170916801414126, validation accuracy: 52.34375% took: 121.00283908843994 seconds
Epoch: 9/10, loss: 1.1397529384184475, validation accuracy: 53.3945% took: 122.36961388587952 seconds
Epoch: 10/10, loss: 1.1141537592762887, validation accuracy: 54.126% took: 122.86240983009338 seconds
Training ended after 10 ! Best validation accuracy: 54.126%
```

#### Size 256

TODO
