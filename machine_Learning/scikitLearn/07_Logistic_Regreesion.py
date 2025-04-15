'''
    로지스틱 회귀
'''
# 공부 시간에 따른 자격증 시험 합격 가능성
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('..\machine_Learning\scikitLearn\LogisticRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# 학습 (로지스틱 회귀 모델)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train,y_train)

# 6시간 공부했을 때 예측
result = classifier.predict([[6]])
print('6시간 공부 했을때 :',result)
# 결과 1 : 합격

# 6시간 공부했을때때 합격할 확률 출력
result = classifier.predict_proba([[6]]) 
print('6시간 공부 예측 :',result)
# 6시간 공부 예측 : [[0.141483 0.858517]]
# 불합격 확률 14%  합력 확률 86%

# 4시간 공부했을 때 예측
result = classifier.predict([[4]])
print('4시간 공부 했을때 :',result)
# 결과 0 : 불합격

'''
    분류 결과 예측(테스트 세트)
'''
y_pred = classifier.predict(X_test)
print('예측 값',y_pred) # 예측 값
# 예측 값 [1 0 1 1] -> [합격,불합격,합격,합격]
print('실제 값',y_test) # 실제 값
# 실제 값 [1 0 1 0] -> [합격,불합격,합격,불합격]

print('공부 시간 :',X_test) # 테스트 세트
# 공부 시간 : [[ 8.6] -[예측 값] 1로 합격, [실제 값] 1로 합격
#             [ 1.2] - [예측 값] 0로 불합격, [실제 값] 0로 불합격
#             [10. ] - [예측 값] 1로 합격, [실제 값] 1로 1합격
#             [ 4.5]] - [예측 값] 1로 합격, [실제 값] 0로 불합격

print(classifier.score(X_test,y_test)) # 모델 평가, 0.75
# 전체 테스트 세트 4개 중에서 분류 예측을 올바로 맞힌 개수 3개 -> 3/4 = 0.75

'''
    데이터 시각화(훈련 세트)
'''
# X의 최소값부터 X의 최대값까지 0.1 단위로 나눔
X_range = np.arange(min(X),max(X),0.1)
# print(X_range) # 결과값 : 0.5 0.6 0.7 0.8 0.9 ....

# p = 1 /(1+e^y) # 로지스틱 회귀에서 사용되는 로지스틱 함수
# p = 1 /(1+np.exp(-y))
p = 1/(1+np.exp(-(classifier.coef_ * X_range + classifier.intercept_))) # y = mx + b
# print(p.shape) # 결과값 : (1,95) 2차원 배열
# print(X_range.shape) # 결과값 : (95,) 1차원 배열

p = p.reshape(-1) # 1차원 배열 형태로 변경

plt.scatter(X_train,y_train,color='blue')
plt.plot(X_range,p,color='green')
# X_range 개수만큼 0.5로 가득찬 배열 만들기
plt.plot(X_range,np.full(len(X_range),0.5),color='red')

plt.title('Probability by hours')
plt.xlabel('hour')
plt.ylabel('P')
plt.show()
 
'''
    테스트 시각화(테스트 세트)
'''
plt.scatter(X_test,y_test,color='blue')
plt.plot(X_range,p,color='green')
# X_range 개수만큼 0.5로 가득찬 배열 만들기
plt.plot(X_range,np.full(len(X_range),0.5),color='red')

plt.title('Probability by hours(test)')
plt.xlabel('hour')
plt.ylabel('P')
plt.show()

'''
    혼동 행렬(Confusion Matrix)
'''
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
# [결과값]
# [[1 1]
#  [0 2]]

# TRUE NEGATIVE (TN)               # FALSE POSITIVE (FP)
# 불합격 (예측) - [결과값]의 (0,0)  # 합격 (예측) - [결과값]의 (0,1)
# 불합격 (실제)                     # 불합격 (실제)

# FALSE NEGATIVE (FN)              # TRUE POSITIVE (TP)
# 불합격 (예측) - [결과값]의 (1,0)  # 합격 (예측) - [결과값]의 (1,1)
# 합격 (실제)                       # 합격 (실제)