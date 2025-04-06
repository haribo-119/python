'''
    선형회귀
'''
# 공부 시간에 따른 시험 점수
import matplotlib.pyplot as plt # 그래프
import pandas as pd # 데이터 조작 및 분석을 위한 강력한 라이브러리

dataset = pd.read_csv('..\machine_Learning\scikitLearn\LinearRegressionData.csv')

# X는 [독립변수]  
# .iloc[row,col] 모든 독립변수의 값을 가져옴
X = dataset.iloc[:,:-1].values
# Y는 [종속변수]
y = dataset.iloc[:,-1].values
print(X,y)

from sklearn.linear_model import LinearRegression # 머신러닝을 위한 Python 라이브러리
reg = LinearRegression() # 객체 생성성

# 조건 : X가 2차원 배열, y는 1차원 배열이여 한다
reg.fit(X,y) # 학습(모델 생성)

'''학습된 모델로 결과를 도출'''
# predict는 2차원 배열만 받음
y_pred = reg.predict(X)
print(y_pred)

plt.scatter(X,y,color='blue') # 산점도
plt.plot(X,y_pred,color='green') # 선 그래프
plt.title('Score by hours')
plt.xlabel('hours') # X축 이름
plt.ylabel('score') # Y축 이름
plt.show()

#reg.predict([[9]])에서 [[9]]가 2차원 배열이 되는 이유,
#Python에서 리스트를 중첩하여 배열의 차원을 정의
print('9시간 공부했을 때 예상 점수 : ',reg.predict([[9]]))

# y = mx + b : 선 그래프
print('기울기 :', reg.coef_) # 기울기(m)
print('y 절편 :', reg.intercept_) # y 절편 (b)