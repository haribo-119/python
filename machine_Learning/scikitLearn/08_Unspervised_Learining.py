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
# plt.scatter(X[:,0],X[:,1]) # x축:hour, y축 : score
# plt.title('Score by hours')
# plt.xlabel('hours')  
# plt.xlim(0,100)  # x축 단위 : 0 ~ 100까지
# plt.ylabel('score') 
# plt.ylim(0,100)  # y축 단위 : 0 ~ 100까지
# plt.show()

'''
    피처 스케일링(Feature Scaling)
'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# X의 데이터 대해서 자동으로 스켈링 적용후  X1으로 저장
X1 = sc.fit_transform(X)
# print(X1)

'''
    데이터 시각화(스케일링된 데이터)
'''
## figure 그래프 사이즈 조절
# plt.figure(figsize=(5,5))
# plt.scatter(X1[:,0],X1[:,1])
# plt.title('Score by hours')
# plt.xlabel('hours')
# plt.ylabel('score')
# plt.show()

'''
    최적의 K 값 찾기(엘보우 방식)
'''
from sklearn.cluster import KMeans
# inertia_list = []
# for i in range(1,11) :
#     # KMeans 객체 생성, k-means++ 
#     kmeans = KMeans(n_clusters=i,init='k-means++',random_state = 0)
#     # 모델 학습
#     kmeans.fit(X1)
#     # 각 지점으로부터 클로스터의 중심 까지의 거리의 제곱의 합
#     inertia_list.append(kmeans.inertia_) 

# plt.plot(range(1,11),inertia_list)
# plt.title('Elbow Method')
# plt.xlabel('n_clusters')
# plt.ylabel('inertia')
# plt.show()

## K = 4 # 최적의 K 값

'''
    최적의 K(4) 값으로 KMeans 학습
'''
K = 4
kmeans = KMeans(n_clusters=K, random_state = 0)
# kmeans.fit(X1)
y_kmeans = kmeans.fit_predict(X1)
print(y_kmeans)


'''
    데이터 시각화 (최적의 K)
'''
# 클러스터의 중심점 좌표
centers = kmeans.cluster_centers_
# print(centers)

# for cluster in range(K) :
#     plt.scatter(X1[y_kmeans == cluster,0], X1[y_kmeans == cluster,1], s =100, edgecolors='black')
#     plt.scatter(centers[cluster,0], # X 좌표 0
#                 centers[cluster,1], # y 좌표 1
#                 s=300, 
#                 edgecolors='black',color='yellow',marker='s')
#     plt.text(centers[cluster,0], # X 좌표 0
#              centers[cluster,1], # y 좌표 1)
#              cluster,va='center',ha='center')
# plt.title('Score by hours')
# plt.xlabel('hours')
# plt.ylabel('score')
# plt.show()

'''
    데이터 시각화 (스케일링 원복)
'''
# Feature Scaling 된 데이터를 다시 원복
X1_org = sc.inverse_transform(X1)
# print(X_org[:5])

centers_org = sc.inverse_transform(centers)
# print(centers_org)

for cluster in range(K) :
    plt.scatter(X1_org[y_kmeans == cluster,0], X1_org[y_kmeans == cluster,1], s =100, edgecolors='black')
    plt.scatter(centers_org[cluster,0], # X 좌표 0
                centers_org[cluster,1], # y 좌표 1
                s=300, 
                edgecolors='black',color='yellow',marker='s')
    plt.text(centers_org[cluster,0], # X 좌표 0
             centers_org[cluster,1], # y 좌표 1)
             cluster,va='center',ha='center')
plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()