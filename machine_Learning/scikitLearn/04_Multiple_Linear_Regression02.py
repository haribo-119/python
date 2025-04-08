'''
    원-핫 인코딩
'''
import pandas as pd
dataset = pd.read_csv('..\machine_Learning\scikitLearn\MultipleLinearRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

'''다중 공선성'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# transformers=[('encoder',OneHotEncoder(다중공선성),
# [컬럼 인덱스])],원-핫 인코딩을 적용하지 않는 나머지는 그대로 둔다
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(drop='first'),[2])],remainder='passthrough')
X = ct.fit_transform(X)

#print(X)
# [1.0 0.0 0.5 3] -> 1,0 Home (1.0 0.0)
# [0.0 1.0 1.2 4] -> 0,1 Library (0.0 1.0)
# [0.0 0.0 1.8 2] -> 0,0 Cafe (0.0 0.0)

'''
    다중 선형 회귀
'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

'''학습(다중 선형 회귀)'''
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,y_train)

'''예측 값과 실제 값 비교 테스트'''
y_pred = reg.predict(X_test)
print(y_pred) 
print(y_test)
print(reg.coef_)
print(reg.intercept_)

'''모델 평가'''
print('훈련세트',reg.score(X_train,y_train))
print('테스트세트',reg.score(X_test,y_test))