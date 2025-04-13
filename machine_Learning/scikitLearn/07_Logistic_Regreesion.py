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