'''
    K-Means
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('..\machine_Learning\scikitLearn\KMeansData.csv')

X = dataset.iloc[:,:].values
# X = dataset.values ==  X = dataset.iloc[:,:].values과 동일
# X = dataset.to_numpy()  # 공식 홈페이지 권장

'''
  데이터 시각화 (전체 데이터 분포 확인)
'''
# plt.scatter(X[:,0],X[:,1]) # x축:hour, y축 : score
# plt.title('Score by hours')
# plt.xlabel('hours') # x축 단위 : 0 ~ 10까지 
# plt.ylabel('score') # y축 단위 : 0 ~ 100까지
# plt.show()

'''
  데이터 시각화(축 범위 통일)
'''
plt.scatter(X[:,0],X[:,1]) # x축:hour, y축 : score
plt.title('Score by hours')
plt.xlabel('hours')  
plt.xlim(0,100)  # x축 단위 : 0 ~ 100까지
plt.ylabel('score') 
plt.ylim(0,100)  # y축 단위 : 0 ~ 100까지
plt.show()

'''
    피처 스케일링(Feature Scaling)
'''