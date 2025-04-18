import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('..\machine_Learning\scikitLearn\QuizData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,y_train)

'''
    데이터 시각화(훈련 세트)
'''
y_pred = reg.predict(X_train)

plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train,y_pred,color='green')
plt.title('efficient')
plt.xlabel('total')
plt.ylabel('reception')
plt.show()

'''
    데이터 시각화(테스트 세트)
'''
plt.scatter(X_test,y_test,color='blue')
#plot 그대로 두는 이유 : 훈련 모델이 그려진 것을 바탕으로 테스트 위치 확인
plt.plot(X_train,y_pred,color='green')
plt.title('efficient')
plt.xlabel('total')
plt.ylabel('reception')
plt.show()

'''
    훈련 세트, 테스트 세트 평가
'''
print('훈련 세트 점수 : ',reg.score(X_train,y_train))
print('테스트 세트 점수 : ', reg.score(X_test,y_test))

'''
    결혼식 참석 인원이 300명일 때 예상되는 식수 인원을 구하시오
'''
total = 300 # 결혹식 참석 인원
y_pred = reg.predict([[total]])
print(y_pred) # 결과 값 [176.92793218]
print(np.around(y_pred[0]).astype(int))  # 결과값 : 177
# 예상되는 식수 인원 약 177명

