# 11주차
from tensorflow import tf
tf.__version__  #tensroflow의 버전을 확인하는함수
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    raise SystemError('GPU device not found')
print('Found GPU')

# 파일 선택을 통해 예제 데이터를 내 컴퓨터에서 불러옵니다.
from google.colab import files
uploaded = files.upload()
my_data = 'ThoraricSurgery.csv'
# 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# 필요한 라이브러리를 불러옵니다.
import numpy as np
import tensorflow as tf
# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
np.random.seed(3)
tf.random.set_seed(3)
# 불러온 데이터를 적용합니다.
Data_set = np.loadtxt(my_data, delimiter=",")
# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장합니다.
X = Data_set[:,0:17] #그냥 인덱스 슬라이싱
Y = Data_set[:,17]
# 딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다).
model = Sequential() #순차적 구성
model.add(Dense(30, input_dim=17, activation='relu'))#30개의 노드로 이루어진 차원이 17 사용은 relu
model.add(Dense(1, activation='sigmoid'))#노드가 하나인 레이어 추가
# 딥러닝을 실행합니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) #구성한 모듈을 컴파일
model.fit(X, Y, epochs=100, batch_size=10) # X, Y를 가지고 실행 batch size는 10명씩

#12주차 선형회귀

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#공부시간 X와 성적 Y의 리스트를 만듭니다.
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]
#그래프로 나타내 봅니다.
plt.figure(figsize=(8,5)) #데이터 시각화
plt.scatter(x, y)
plt.show()
#리스트로 되어 있는 x와 y값을 넘파이 배열로 바꾸어 줍니다.(인덱스를 주어 하나씩 불러와 계산이 가능해 지도록 하기 위함입니다.)
x_data = np.array(x)
y_data = np.array(y)
# 기울기 a와 절편 b의 값을 초기화 합니다.
a = 0
b = 0
#학습률을 정합니다.
lr = 0.03
#몇 번 반복될지를 설정합니다.
epochs = 2001
#경사 하강법을 시작합니다.
for i in range(epochs): # epoch 수 만큼 반복
    y_hat = a * x_data + b  #y를 구하는 식을 세웁니다
    error = y_data - y_hat  #오차를 구하는 식입니다.
    a_diff = -(2/len(x_data)) * sum(x_data * (error)) # 오차함수를 a로 미분한 값입니다.
    b_diff = -(2/len(x_data)) * sum(error)  # 오차함수를 b로 미분한 값입니다.
    a = a - lr * a_diff  # 학습률을 곱해 기존의 a값을 업데이트합니다.
    b = b - lr * b_diff  # 학습률을 곱해 기존의 b값을 업데이트합니다.
    if i % 100 == 0:    # 100번 반복될 때마다 현재의 a값, b값을 출력합니다.
        print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))
# 앞서 구한 기울기와 절편을 이용해 그래프를 그려 봅니다.
y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()


#13주차 파마 인디언 당뇨병 데이터 정(형데이터 예시)
# 파일 선택을 통해 예제 데이터를 내 컴퓨터에서 불러옵니다.
from google.colab import files
uploaded = files.upload()
my_data = 'pima-indians-diabetes.csv'
# pandas 라이브러리를 불러옵니다.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 불러온 데이터셋을 적용합니다. 이 때 각 컬럼에 해당하는 이름을 지정합니다.
df = pd.read_csv(my_data, names = ["pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"])
# 처음 5줄을 봅니다.
print(df.head(5))
# 데이터의 전반적인 정보를 확인해 봅니다.
print(df.info())
# 각 정보별 특징을 좀더 자세히 출력합니다.
print(df.describe())
# 데이터 중 임신 정보와 클래스 만을 출력해 봅니다.
print(df[['plasma', 'class']])
# 데이터 간의 상관관계를 그래프로 표현해 봅니다.
colormap = plt.cm.gist_heat   #그래프의 색상 구성을 정합니다.
plt.figure(figsize=(12,12))   #그래프의 크기를 정합니다.
# 그래프의 속성을 결정합니다. vmax의 값을 0.5로 지정해 0.5에 가까울 수록 밝은 색으로 표시되게 합니다.
sns.heatmap(df.corr(),linewidths=0.1,vmax=0.5, cmap=colormap, linecolor='white', annot=True)
plt.show()
grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma',  bins=10)
plt.show()
# 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 필요한 라이브러리를 불러옵니다.
import numpy
import tensorflow as tf
# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
numpy.random.seed(3)
tf.random.set_seed(3)
# 데이터를 불러 옵니다.
dataset = numpy.loadtxt(my_data, delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]
# 모델을 설정합니다.
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# 모델을 컴파일합니다.
model.compile(loss='binary_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])
# 모델을 실행합니다.
model.fit(X, Y, epochs=200, batch_size=10)
# 결과를 출력합니다.
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))

#손글씨 이미지 분류 (비정형 데이터)

import numpy
import sys
import matplotlib.pyplot as plt
# seed 값 설정
seed = 0
numpy.random.seed(seed)
# MNIST데이터셋 불러오기
(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()
print("학습셋 이미지 수 : %d 개" % (X_train.shape[0]))
print("테스트셋 이미지 수 : %d 개" % (X_test.shape[0]))
# 그래프로 확인
plt.imshow(X_train[0], cmap='Greys') #데이터 시각화
plt.show()
# 코드로 확인
for x in X_train[0]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')
# 차원 변환 과정
X_train = X_train.reshape(X_train.shape[0], 784) #데이터 변환 (60000,28,28) => (60000, 784)
X_train = X_train.astype('float64')
X_train = X_train / 255 #nomalization
X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255 #데이터 변환 위 과정 한번에
#print(X_train[0])
# 클래스 값 확인
print("class : %d " % (Y_class_train[0]))
# 바이너리화 과정
Y_train = np_utils.to_categorical(Y_class_train, 10)
Y_test = np_utils.to_categorical(Y_class_test, 10)
print(Y_train[0])

#14주차 정형 데이터 이중 분류 실습

colormap = plt.cm.gist_heat#그래프 색상 구성을 정합니다
plt.figure(figsize=(12,12))#그래프의 크기를 정합니다
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)
plt.show()

Data_set =df.values #데이터 값 추출
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.colpile() #모델 실행
model.fit()
model.evaluate()

#panama data 실습
dataset = df.values# 데이터 값 추출
X_train = dataset[0:500 ,0:8] # 768 x 9 (dataset) => 500 * 8
Y_train = dataset[0:500,8] #768 *9(dataset) => 500 * 1             학습데이터와 트레이닝 데이터 나누기

# 그 후에 add


#15주차 정형데이터 다중 분류 실습

df = df.sample(frac=1) #데이터 셔플
dataset = df.values
#훈련데이터와 실행데이터 나누기
e1 = LabelEncoder()
e1.fit(Y_train_raw)
Y_train_proc = e1.transfrom(Y_train_raw) #문자열 -> 숫자 변환

# test data = 모델 개발과정에 절대로 활용이 불가능 하다
#cnn과 FFNN의 차이점은 입력이 FFNN은 벡터 CNN은 행렬이며 FFNN은 Dense Layer CNN은 Convolutional layer, pooling layer

model.add(Conv2D(32, kernel_size = (3,3), input_shape=(28,28,1))) # 첫 인자는 마스크의 갯수
# 즉 이미지 데이터는 CNN이 FFNN보다 성능이 우수하다