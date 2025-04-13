'''
    다항 회귀
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('..\machine_Learning\scikitLearn\PolynomialRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
'''
    단순 선형 회귀
'''
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X,y)

# # 단순 선형 회귀 시각화
# plt.scatter(X,y,color='blue') # 그래프의 점(산점도)
# plt.plot(X,reg.predict(X),color='green') # 선그래프
# plt.title('Score by hours') # 제목
# plt.xlabel('hours') # x축 이름
# plt.ylabel('score') # y축 이름
# plt.show()

# print('단순 선형 회귀 평가 :',reg.score(X,y)) # 모델 평가 

'''
    다항 회귀 
'''
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4) # 4차

# poly_reg.fit()
# poly_reg.transform(X) 아래는 한줄로 요약
X_poly = poly_reg.fit_transform(X)

'''
# print(X_poly[:5]) # [x] -> [x^0 + x¹ +  x² ]
print(X_poly[:5]) # 길이가 5까지 출력
 # degree=2, 2차 방정식 
  0     1     2 로 행으로 출력됨
-결과값 예시
[[1.   0.2  0.04]
 [1.   0.5  0.25]
 [1.   0.8  0.64]
 [1.   0.9  0.81]
 [1.   1.2  1.44]]
# print(poly_reg.get_feature_names_out()) 결과값 ['1' 'x0' 'x0^2']
'''
lin_reg = LinearRegression()
lin_reg.fit(X_poly,y) # 변환된 X와 y를 가지고 학습

# 데이터 시각화
# plt.scatter(X,y,color='blue')
# plt.plot(X,lin_reg.predict(X_poly),color='green')
# plt.title('Polynomial Regression')
# plt.xlabel('hours')
# plt.ylabel('score')
# plt.show()

'''
    다항 회귀 그래프 수정
    X 값을 0.1 단위로 잘라서 데이터 형성
'''
# X의 최소값에서 최대값까지의 범위를 0.1 단위로 잘라서 데이터 형성성
X_range = np.arange(min(X),max(X),0.1)
#print(X_range) #1차원 배열로 출력

# reshape(row갯수, 컬럼 갯수)
# reshape()의 -1은 전체 row를 자동으로 넣어줌
X_range = X_range.reshape(-1,1) 

# 데이터 시각화
plt.scatter(X,y,color='blue')
plt.plot(X_range,lin_reg.predict(poly_reg.fit_transform(X_range)),color='green')
plt.title('Polynomial Regression2')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

'''
    공부 시간에 따른 시험 성적 예측
'''
# 2시간 공부했을 때, 선형 회귀 모델 예측
print('선형 회귀(2시간 공부 예측) :',reg.predict([[2]])) # [19.85348988]
print('다항 회귀(2시간 공부 예측) :',lin_reg.predict(poly_reg.fit_transform([[2]]))) #[8.70559135]

