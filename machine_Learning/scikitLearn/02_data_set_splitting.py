'''
    데이터 세트 분리
    
    #이미 가지고 있는 데이터를 
    #[훈련 세트 80%], [테스트 세트 20%]로 나누어서 트레이닝
'''
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('..\machine_Learning\scikitLearn\LinearRegressionData.csv')
X = dataset.iloc[:,:-1].values # :-1 마지막 열을 제외
y = dataset.iloc[:,-1].values # -1은 마지막 열을 선택
# y는 모든 행과 마지막 열을 선택하여 반환

# [훈련세트], [테스트 세트]
from sklearn.model_selection import train_test_split

# test_size=0.2는 [테스트 세트]를 20% 사용하겠다는 의미
# random_state 정해주는 값에 따라 랜덤하게 데이터를 순서를 변경
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)
# print(X_train)                     # print(y_train)
# print(len(X_train)) #16개(80%)     # print(len(y_train)) #16개(80%)
# print(X_test)                      # print(y_test)
# print(len(X_test)) #4개 (20%)      # print(len(y_test)) #4개(20%)

'''분리된 데이터를 통한 모델링'''
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train) # 훈력 세트로 학습

'''데이터 시각화(훈련 세트)'''
# y_pred = reg.predict(X_train)
# print(X_train)

# plt.scatter(X_train,y_train,color='blue')
# plt.plot(X_train,y_pred,color='green')
# plt.title('data set')
# plt.xlabel('hours')
# plt.ylabel('score')
# plt.show()

'''데이터 시각화(테스트 세트)'''
# y_pred = reg.predict(X_test)
# print(X_test)

# plt.scatter(X_test,y_test,color='blue')
# plt.plot(X_test,y_pred,color='green')
# plt.title('test set')
# plt.xlabel('hours')
# plt.ylabel('score')
# plt.show()

print(reg.coef_) # 기울기 (m)
print(reg.intercept_) # y 절편(b)

'''모델 평가'''
print('훈련세트',reg.score(X_test,y_test)) # 테스트 세트를 통한 모델 평가 1이면 100점
print('테스트 세트',reg.score(X_train,y_train))