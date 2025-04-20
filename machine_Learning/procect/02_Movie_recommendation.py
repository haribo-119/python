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
    2. Content Based Filtering (콘텐츠 기반 필터링) 
        - 다양한 요소 기반 추천 (장르,감독,키워드 등)
'''
# print(df2.loc[0,'genres'])
# 결과값 : [{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]
# print(type(df2.loc[0,'genres'])) # 결과값 : <class 'str'>

''' str -> list 변환 예시'''
# s1 = [{"id":28,"name":"Action"}]
# s2 = '[{"id":28,"name":"Action"}]'
# print(type(s1),type(s2)) # 결과값 :<class 'list'> <class 'str'>

# from ast import literal_eval
# s2 = literal_eval(s2)
# print(s2, type(s2)) # 결과값 : [{'id': 28, 'name': 'Action'}] <class 'list'>

from ast import literal_eval

features = ['cast','crew','keywords','genres']
for feature in features :
    df2[feature] = df2[feature].apply(literal_eval)

# print(df2.loc[0,'crew'])

# 감독 정보를 추출
def get_director(x):
    for i in x :
        if i['job'] == 'Director':
            return i['name']
    return np.nan

# df2['director'] 컬럼 생성
df2['director'] = df2['crew'].apply(get_director)
# print(df2['director'].head(10))

# director칼럼에 null 값이 있는지 확인
null_check = df2[df2['director'].isnull()]
print(null_check)
