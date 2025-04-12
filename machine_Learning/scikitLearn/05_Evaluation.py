import pandas as pd
dataset = pd.read_csv('..\machine_Learning\scikitLearn\MultipleLinearRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

'''다중 공선성'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(drop='first'),[2])],remainder='passthrough')
X = ct.fit_transform(X)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

'''학습(다중 선형 회귀)'''
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,y_train)

'''예측 값과 실제 값 비교 테스트'''
y_pred = reg.predict(X_test)

'''
    다양한 평가 지표 (회귀 모델)
'''
# 1) MAE(Mean Absolute Error) : (실제 값과 예측 값) 차이의 절대 값
from sklearn.metrics import mean_absolute_error
#y_test - 실제값으로 사용,  y_pred
MAE = mean_absolute_error(y_test,y_pred) # 실제값, 예측값 -> MAE
print('MAE :',MAE) # MAE : 3.225328518828796

# 2) MSE(Mean Squared Error) : 차이의 제곱
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_test,y_pred)
print('MSE :',MSE) # MSE : 19.900226981514965

# 3) RMSE(Root Mean Squared Error) : 차이의 제곱에 루트
from sklearn.metrics import mean_squared_error
# # sqaured=False 하면, 루트 사용한 값이 출력됨
# RMSE = mean_squared_error(y_test,y_pred,squared=False) # RMSE
# print('RMSE :',RMSE)

import numpy as np
# RMSE 계산
RMSE = np.sqrt(mean_squared_error(y_test, y_pred))  # RMSE
print('RMSE :', RMSE) # RMSE : 4.460967045553572

# 4) R2 : 결정 계수 - 1에 가까울 수록 성능이 좋음
from sklearn.metrics import r2_score
r2 = r2_score(y_test,y_pred)
print('r2 :',r2) # r2 : 0.9859956178877446
print('테스트세트',reg.score(X_test,y_test)) # 테스트세트 0.9859956178877446
# r2_score와 reg.score 값이 같다