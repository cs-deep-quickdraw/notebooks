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
Epoch: 1/10, loss: 3.450085401062042, validation accuracy: 46.44675% took: 222.4983425140381 seconds
Epoch: 2/10, loss: 1.0706067289263068, validation accuracy: 67.308% took: 223.42625331878662 seconds
Epoch: 3/10, loss: 0.7785157866344002, validation accuracy: 73.3275% took: 224.1862027645111 seconds
Epoch: 4/10, loss: 0.673292183615129, validation accuracy: 75.59225% took: 223.58587527275085 seconds
Epoch: 5/10, loss: 0.6154802498394192, validation accuracy: 77.57575% took: 223.44685244560242 seconds
Epoch: 6/10, loss: 0.5785185304628541, validation accuracy: 77.986% took: 222.65764713287354 seconds
Epoch: 7/10, loss: 0.5523939039121895, validation accuracy: 78.9695% took: 223.1387050151825 seconds
Epoch: 8/10, loss: 0.5323585802807205, validation accuracy: 79.4235% took: 225.70758032798767 seconds
Epoch: 9/10, loss: 0.5165840414922857, validation accuracy: 79.55125% took: 225.84810876846313 seconds
Epoch: 10/10, loss: 0.5034468623094426, validation accuracy: 80.3615% took: 221.7098958492279 seconds
Training ended after 10 ! Best validation accuracy: 80.3615%
```


### 2 layer

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
Epoch: 1/10, loss: 2.85440549114427, validation accuracy: 43.80875% took: 159.92264580726624 seconds
Epoch: 2/10, loss: 1.3070660994023287, validation accuracy: 59.8185% took: 160.52830529212952 seconds
Epoch: 3/10, loss: 1.002111164056948, validation accuracy: 65.979% took: 160.42838668823242 seconds
Epoch: 4/10, loss: 0.8725508252118471, validation accuracy: 69.00175% took: 159.8428339958191 seconds
Epoch: 5/10, loss: 0.7979135324947968, validation accuracy: 71.179% took: 160.1855492591858 seconds
Epoch: 6/10, loss: 0.7501726136361074, validation accuracy: 72.32525% took: 160.2415418624878 seconds
Epoch: 7/10, loss: 0.7173503141549368, validation accuracy: 73.697% took: 160.5984365940094 seconds
Epoch: 8/10, loss: 0.6923283491925913, validation accuracy: 74.4915% took: 161.3248324394226 seconds
Epoch: 9/10, loss: 0.673028680673409, validation accuracy: 75.13575% took: 160.56888151168823 seconds
Epoch: 10/10, loss: 0.656578666564522, validation accuracy: 75.8965% took: 160.4016330242157 seconds
Training ended after 10 ! Best validation accuracy: 75.8965%
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
Epoch: 1/10, loss: 2.241943362113777, validation accuracy: 68.43325% took: 551.8330771923065 seconds
Epoch: 2/10, loss: 0.7178280552393584, validation accuracy: 77.101% took: 552.4268352985382 seconds
Epoch: 3/10, loss: 0.568413649472906, validation accuracy: 80.37875% took: 556.9509761333466 seconds
Epoch: 4/10, loss: 0.5019938328381951, validation accuracy: 81.4775% took: 553.2961277961731 seconds
Epoch: 5/10, loss: 0.4595997158195273, validation accuracy: 82.874% took: 553.0105752944946 seconds
Epoch: 6/10, loss: 0.42786897372554056, validation accuracy: 83.26475% took: 557.2912697792053 seconds
Epoch: 7/10, loss: 0.4011682662366676, validation accuracy: 83.07625% took: 552.2755541801453 seconds
Epoch: 8/10, loss: 0.37829458634000146, validation accuracy: 83.33875% took: 551.1248097419739 seconds
Epoch: 9/10, loss: 0.35719512086602434, validation accuracy: 83.512% took: 552.0249559879303 seconds
Epoch: 10/10, loss: 0.3381216313070575, validation accuracy: 83.45275% took: 551.1745088100433 seconds
Training ended after 10 ! Best validation accuracy: 83.512%
```

## Conv1D LSTM

### 1 layer

#### Conv 128_5 size 64

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
conv1 = (128, 5)
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
Epoch: 1/10, loss: 2.4521238011677897, validation accuracy: 42.35875% took: 140.67531204223633 seconds
Epoch: 2/10, loss: 1.480470366893284, validation accuracy: 49.781% took: 139.75940108299255 seconds
Epoch: 3/10, loss: 1.2990560588451563, validation accuracy: 51.917% took: 139.11033821105957 seconds
Epoch: 4/10, loss: 1.2144290166857543, validation accuracy: 54.22025% took: 139.14547657966614 seconds
Epoch: 5/10, loss: 1.161270840165253, validation accuracy: 56.294% took: 138.57833814620972 seconds
Epoch: 6/10, loss: 1.12227923897093, validation accuracy: 56.4285% took: 138.07167291641235 seconds
Epoch: 7/10, loss: 1.0923172702911979, validation accuracy: 57.21075% took: 138.1560935974121 seconds
Epoch: 8/10, loss: 1.0696373967985238, validation accuracy: 57.8435% took: 140.04968333244324 seconds
Epoch: 9/10, loss: 1.049920146655719, validation accuracy: 58.2105% took: 138.90221500396729 seconds
Epoch: 10/10, loss: 1.0328531821558635, validation accuracy: 59.2585% took: 138.53191256523132 seconds
Training ended after 10 ! Best validation accuracy: 59.2585%
```

#### Conv 128_5 size 256

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
conv1 = (128, 5)
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
Epoch: 1/10, loss: 1.7443331885197457, validation accuracy: 65.8505% took: 223.55910396575928 seconds
Epoch: 2/10, loss: 0.8100666383439411, validation accuracy: 72.96875% took: 224.83714652061462 seconds
Epoch: 3/10, loss: 0.6820556036522427, validation accuracy: 76.34125% took: 223.60430526733398 seconds
Epoch: 4/10, loss: 0.6185645249571032, validation accuracy: 77.35375% took: 224.03959131240845 seconds
Epoch: 5/10, loss: 0.5787777861025488, validation accuracy: 78.771% took: 223.8713116645813 seconds
Epoch: 6/10, loss: 0.5516596786552914, validation accuracy: 79.35025% took: 224.39657926559448 seconds
Epoch: 7/10, loss: 0.5306601781161085, validation accuracy: 79.93475% took: 223.9412078857422 seconds
Epoch: 8/10, loss: 0.5149018921842041, validation accuracy: 80.4145% took: 224.26603865623474 seconds
Epoch: 9/10, loss: 0.5012614039121784, validation accuracy: 80.6875% took: 224.92499136924744 seconds
Epoch: 10/10, loss: 0.4899136547157039, validation accuracy: 80.99125% took: 223.96182942390442 seconds
Training ended after 10 ! Best validation accuracy: 80.99125%
```


### 2 layers

#### Conv 128_5 size 128

Config:
```python
# Config:
batch_size = 256
learning_rate = 0.001

hidden_size = 128
n_layers = 2
train_classes = classes[:]

# Use None instead of (n_filters, filter_size) to disable convolution
# Note that conv1 = None forces conv2 = None automatically
conv1 = (128, 5)
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
Epoch: 1/10, loss: 1.8820938994450254, validation accuracy: 65.623% took: 193.96429586410522 seconds
Epoch: 2/10, loss: 0.8107301404507292, validation accuracy: 73.586% took: 194.17708706855774 seconds
Epoch: 3/10, loss: 0.6735798475013932, validation accuracy: 77.1175% took: 193.86641478538513 seconds
Epoch: 4/10, loss: 0.6112821575363391, validation accuracy: 78.4195% took: 194.2947657108307 seconds
Epoch: 5/10, loss: 0.5740221543591596, validation accuracy: 79.65825% took: 194.48485040664673 seconds
Epoch: 6/10, loss: 0.548403986350501, validation accuracy: 80.2055% took: 193.7735493183136 seconds
Epoch: 7/10, loss: 0.5292938662089506, validation accuracy: 80.5225% took: 194.6201422214508 seconds
Epoch: 8/10, loss: 0.5142936285084041, validation accuracy: 80.89625% took: 194.2792673110962 seconds
Epoch: 9/10, loss: 0.5025446949695695, validation accuracy: 81.58775% took: 194.51082038879395 seconds
Epoch: 10/10, loss: 0.4924990823078778, validation accuracy: 81.69775% took: 194.03370189666748 seconds
Training ended after 10 ! Best validation accuracy: 81.69775%
```


## Conv1D BiLSTM

### 2 Layers

#### Conv 256_5 Size 256

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
conv1 = (256, 5)
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
Epoch: 1/10, loss: 1.3588914447277498, validation accuracy: 69.3735% took: 629.1327741146088 seconds
Epoch: 2/10, loss: 0.7110744219887932, validation accuracy: 75.29825% took: 628.8111436367035 seconds
Epoch: 3/10, loss: 0.6004638118550427, validation accuracy: 78.38275% took: 629.9860546588898 seconds
Epoch: 4/10, loss: 0.5388856523323499, validation accuracy: 79.79525% took: 629.3414313793182 seconds
Epoch: 5/10, loss: 0.49726788932880733, validation accuracy: 80.86525% took: 628.2816607952118 seconds
Epoch: 6/10, loss: 0.4649494013308136, validation accuracy: 81.2705% took: 627.375824213028 seconds
Epoch: 7/10, loss: 0.43812784456831383, validation accuracy: 81.55875% took: 627.1648995876312 seconds
Epoch: 8/10, loss: 0.41473025375919703, validation accuracy: 82.0465% took: 630.023939371109 seconds
Epoch: 9/10, loss: 0.39390789862861864, validation accuracy: 82.17925% took: 629.4058969020844 seconds
Epoch: 10/10, loss: 0.37503225241430005, validation accuracy: 82.168% took: 627.2750012874603 seconds
Training ended after 10 ! Best validation accuracy: 82.17925%
```

#### Conv 128_3 Size 256

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
conv1 = (128, 3)
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
Epoch: 1/10, loss: 1.4458234518457433, validation accuracy: 70.179% took: 630.9494168758392 seconds
Epoch: 2/10, loss: 0.6833124341800547, validation accuracy: 77.27725% took: 630.3967542648315 seconds
Epoch: 3/10, loss: 0.5669822885195821, validation accuracy: 79.38775% took: 629.7384443283081 seconds
Epoch: 4/10, loss: 0.5058896666785812, validation accuracy: 81.322% took: 630.7445013523102 seconds
Epoch: 5/10, loss: 0.4642114854283878, validation accuracy: 81.59575% took: 630.1018018722534 seconds
Epoch: 6/10, loss: 0.43246729940111167, validation accuracy: 82.56975% took: 630.7682511806488 seconds
Epoch: 7/10, loss: 0.4056210992935295, validation accuracy: 82.552% took: 629.5818972587585 seconds
Epoch: 8/10, loss: 0.38292044424818433, validation accuracy: 82.611% took: 630.5734429359436 seconds
Epoch: 9/10, loss: 0.3625405829137104, validation accuracy: 83.031% took: 631.2119917869568 seconds
Epoch: 10/10, loss: 0.34431914681740156, validation accuracy: 82.712% took: 630.0399312973022 seconds
Training ended after 10 ! Best validation accuracy: 83.031%
```

## Double Conv1D BiLSTM

### 2 Layers

#### Conv 256_5 Conv 256_3 Size 256

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
conv1 = (256, 5)
conv2 = (256, 3)
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
Epoch: 1/10, loss: 1.5147245427595735, validation accuracy: 68.9645% took: 661.1092238426208 seconds
Epoch: 2/10, loss: 0.7550979995947251, validation accuracy: 76.213% took: 660.7555015087128 seconds
Epoch: 3/10, loss: 0.6128813853249208, validation accuracy: 79.1695% took: 660.8972115516663 seconds
Epoch: 4/10, loss: 0.5423832523918909, validation accuracy: 80.61375% took: 662.6243762969971 seconds
Epoch: 5/10, loss: 0.496023634312996, validation accuracy: 81.58625% took: 662.6504101753235 seconds
Epoch: 6/10, loss: 0.46180859410654457, validation accuracy: 82.0125% took: 662.0622477531433 seconds
Epoch: 7/10, loss: 0.4341143711888346, validation accuracy: 82.42775% took: 662.0534932613373 seconds
Epoch: 8/10, loss: 0.4125720049776342, validation accuracy: 82.784% took: 662.8852000236511 seconds
Epoch: 9/10, loss: 0.39086888840954387, validation accuracy: 82.508% took: 661.7064199447632 seconds
Epoch: 10/10, loss: 0.37362678031655594, validation accuracy: 82.7225% took: 662.1078498363495 seconds
Training ended after 10 ! Best validation accuracy: 82.784%
```

#### Conv 256_5 Conv 256_3 Size 256 all dataset

Results:
```
Epoch: 1/20, loss: 0.8977765124025161, validation accuracy: 81.04190789473684% took: 2578.4268980026245 seconds
Epoch: 2/20, loss: 0.4893854798543802, validation accuracy: 84.74578947368421% took: 2589.1363003253937 seconds
Epoch: 3/20, loss: 0.4322637861393286, validation accuracy: 85.78394736842105% took: 2607.142402648926 seconds
Epoch: 4/20, loss: 0.40336743451813517, validation accuracy: 86.69552631578948% took: 2597.696293115616 seconds
Epoch: 5/20, loss: 0.3838846281314396, validation accuracy: 86.77006578947369% took: 2592.3787355422974 seconds
Epoch: 6/20, loss: 0.36994369611107925, validation accuracy: 87.185% took: 2588.8523235321045 seconds
Epoch: 7/20, loss: 0.3580974556532784, validation accuracy: 87.16203947368422% took: 2605.101353406906 seconds
Epoch: 8/20, loss: 0.348914482592392, validation accuracy: 87.22776315789474% took: 2597.8685224056244 seconds
Epoch: 9/20, loss: 0.3412577998715249, validation accuracy: 87.62743421052632% took: 2586.1124682426453 seconds
Epoch: 10/20, loss: 0.3349219043424182, validation accuracy: 87.53440789473684% took: 2592.396100282669 seconds
Epoch: 11/20, loss: 0.32902332258189154, validation accuracy: 87.54552631578947% took: 2584.8693466186523 seconds
Epoch: 12/20, loss: 0.3227261560952742, validation accuracy: 87.72572368421052% took: 2586.1872086524963 seconds
Epoch: 13/20, loss: 0.3171522105988532, validation accuracy: 87.8621052631579% took: 2591.189444065094 seconds
Epoch: 14/20, loss: 0.3122778429447243, validation accuracy: 87.86098684210526% took: 2593.339725971222 seconds
Epoch: 15/20, loss: 0.3077770005510048, validation accuracy: 87.96967105263158% took: 2585.960666656494 seconds
Epoch: 16/20, loss: 0.30343102741679334, validation accuracy: 87.8471052631579% took: 2601.619851589203 seconds
Epoch: 17/20, loss: 0.30020415274528234, validation accuracy: 87.76105263157895% took: 2593.150027513504 seconds
Epoch: 18/20, loss: 0.2963183523860703, validation accuracy: 87.83861842105263% took: 2587.088585615158 seconds
Epoch: 19/20, loss: 0.2926984957221828, validation accuracy: 87.67842105263158% took: 2587.9735493659973 seconds
Epoch: 20/20, loss: 0.2900448494380763, validation accuracy: 87.51361842105263% took: 2591.950215816498 seconds
Training ended after 20 ! Best validation accuracy: 87.96967105263158%
Test accuracy: 87.44263157894737%
```
