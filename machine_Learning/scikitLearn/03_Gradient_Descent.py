
import pandas as pd

dataset = pd.read_csv('..\machine_Learning\scikitLearn\LinearRegressionData.csv')
X = dataset.iloc[:,:-1].values # :-1 마지막 열을 제외
y = dataset.iloc[:,-1].values # -1은 마지막 열을 선택

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)


'''
    경사 하강법
'''
# 경사 하강법은 자원과 시간이 오래 걸림
# SGD : Stochastic Gradient Descent 확률적 경사 하강법
from sklearn.linear_model import SGDRegressor
# sr = SGDRegressor() # 기본형
# max_iter=훈련횟수, eta0=학습률, random_state=0, verbose=1-훈련을하면서 손실을 줄이는것을 보여준다)
# eta0=0.001과 eta0=1e-3 (지수표기법) 같다
sr = SGDRegressor(max_iter=1000, eta0=0.001, random_state=0,verbose=1) 
sr.fit(X_train, y_train)

import matplotlib.pyplot as plt
plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train,sr.predict(X_train),color='green')
plt.title('Score by hours(train data, SGD)')
plt.xlabel('houts')
plt.ylabel('score')
plt.show()

print('기울기',sr.coef_)
print('절편',sr.intercept_)

# 모델 평가
print('테스트 세트',sr.score(X_test,y_test))
print('확률적 경사하강법',sr.score(X_train,y_train))