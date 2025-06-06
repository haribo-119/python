'''
    영화 추천 시스템
        1) Demographic Filtering (인구통계학적 필터링)
        2) Content Based Filtering (콘텐츠 기반 필터링)
        3) Collaborative Filtering (협업 필터링)
'''
 
''' 1. Demographic Filtering (인구동계학적 필터링) '''
import pandas as pd
import numpy as np

df1 = pd.read_csv('../machine_Learning/procect/tmdb_5000_credits.csv')
df2 = pd.read_csv('../machine_Learning/procect/tmdb_5000_movies.csv')
print(df1.shape,df2.shape) # 결과값 : (4803, 4) (4803, 20)
print(df1['title'].equals(df2['title'])) # True, df1과 df2의 title 칼럼의 데이터가 같다

## tmdb_5000_credits.csv 데이터를 -> tmdb_5000_movies.csv에 병합
# print(df1.columns) # 결과값 : Index(['movie_id', 'title', 'cast', 'crew'], dtype='object')
df1.columns = ['id', 'title', 'cast', 'crew']
# print(df1.columns) # 결과값 : Index(['id', 'title', 'cast', 'crew'], dtype='object')
df1[['id', 'cast', 'crew']] # ['id','cast', 'crew'] 항목만 출력

# df1 -> df2 데이터 머징 
df2 = df2.merge(df1[['id', 'cast', 'crew']], on ='id')
# print(df2.head(3)) # 머징된 데이터 확인

# 모든 영화의 평균 점수
C = df2['vote_average'].mean()
# print(C) # 결과값 : 6.092171559442016

# 상위 10% 데이터를 뽑아 준다
m = df2['vote_count'].quantile(0.9)
# print(m) # 결과값 : 1838.4000000000015

# 1838개 이상의 평가를 가진 영화를 추천
q_movies = df2.copy().loc[df2['vote_count'] >= m]
print(q_movies.shape)

vote_count = q_movies['vote_count'].sort_values()
# print(vote_count) # 인덱스, 추천수 출력 

def weghited_rating(x, m=m, C=C) :
    v = x['vote_count']
    R = x['vote_average']
    # https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system 참조
    return (v / (v + m)*R +(m /(m + v)) * C) 


# apply(적용할 함수), q_movies의 모든 데이터를 적용할 함수
# axis = 1, 행(row) / xis = 0 , 열(column)
q_movies['score'] = q_movies.apply(weghited_rating, axis = 1)
# ascending=False , 내림차순 / 생략시, 오름차순
q_movise = q_movies.sort_values('score', ascending=False)

information = q_movies[['id','title','vote_count','score']].head(10)
# print(information)

'''
    데이터 시각화
'''
# pop= df2.sort_values('popularity', ascending=False)
# import matplotlib.pyplot as plt
# plt.figure(figsize=(12,4))

# plt.barh(pop['title'].head(10),pop['popularity'].head(10), align='center',
#         color='skyblue')
# plt.gca().invert_yaxis()
# plt.xlabel("Popularity")
# plt.title("Popular Movies")
# plt.show()


''' 
    2. Content Based Filtering (콘텐츠 기반 필터링) 
        - 줄거리 기반
'''
df2['overview'].head()

# 피처 벡터화
# TF-IDF 단어의 중요도를 평가하는 방법
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
# print(ENGLISH_STOP_WORDS) # stop_words='english'의 필요없는 단어를 제외
tfidf = TfidfVectorizer(stop_words='english')

# df2에 null 값이 하나라도 존재하면 True
# df2_null = df2['overview'].isnull().values.any()
# print(df2_null) # 결과값 : True

# fillna('') : null 값에 ''(빈문자열)로 채워준다
df2['overview'] = df2['overview'].fillna('')
# df2['overview'] 값을 피처 벡터화
tfidf_matrix = tfidf.fit_transform(df2['overview'])
print(tfidf_matrix.shape) # 결과값 : (4803, 20978)
# 4803(로우) 문서에, 20978(칼럼)개의 단어로 이루어짐
print(tfidf_matrix)
# 결과값 : <Compressed Sparse Row sparse matrix of dtype 'float64'
#           with 125840 stored elements and shape (4803, 20978)>

# 유사도 판단
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# print(cosine_sim)

# 영화 추천
indices = pd.Series(df2.index,index=df2['title']).drop_duplicates()
# print(indices) # 결과값 : The Dark Knight Rises        3
# print(indices['The Dark Knight Rises']) # 결과값 : 3
# print(df2.iloc[[3]]) # 결과값 : 인덱스 3의 대한 행(row) 정보를 모두 가져온다

'''영화의 제목을 입력받으면 가장 코사인 유사도가 높은 영화 리스트를 출력'''
def get_recommendations(title,cosine_sim=cosine_sim) :
    # 1) 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = indices[title]
    # 2) 코사인 유사도 매트릭스 (consine_sim)에서 idx 에 해당하는 데이터를 (idx,유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    # 3) 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x : x[1], reverse=True)
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    # 4) 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]
    # 5) 인덱스 정보를 통해 영화 제목 추출
    return df2['title'].iloc[movie_indices]


list_movies = get_recommendations('Avengers: Age of Ultron')
print(list_movies)

# ''' 
#     get_recommendations 함수 테스트 
# '''
# # 1) 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
# test_idx = indices['The Dark Knight Rises'] 
# # print(test_idx) #  결과값 : 3

# # 2) 코사인 유사도 매트릭스 (consine_sim)에서 idx 에 해당하는 데이터를 (idx,유사도) 형태로 얻기
# test_sim_scores = list(enumerate(cosine_sim[3]))

# # 3) 코사인 유사도 기준으로 내림차순 정렬
# # sort() : 원본 데이터에서 변경, sorted() : 원본 X, 변경된 데이터를 저장
# test_sim_scores = sorted(test_sim_scores, key=lambda x : x[1], reverse=True)
# print(test_sim_scores[1:11]) # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱

# '''람다식 변경전'''
# def get_second(x):
#     return x[1]

# lst = ['인덱스','유사도']
# print(get_second(lst)) # 결과값 : 유사도

# '''람다식 변경후'''
# result = (lambda x : x[1])(lst) 
# print(result) # 결과값 : 유사도

# # 4) 추천 영화 목록 10개의 인덱스 정보 추출
# test_movie_indices = [i[0] for i in test_sim_scores[1:11]]
# print(test_movie_indices)

# # 5) 인덱스 정보를 통해 영화 제목 추출
# moviseList= df2['title'].iloc[test_movie_indices]
# print(moviseList)