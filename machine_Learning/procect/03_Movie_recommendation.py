'''
    Collaborative Filtering (협업 필터링:사용자 리뷰 기반)

    예시)    나     : up, 주토피아
          다른 사람 : up, 주토피아, 인사이드 아웃

    >> 인사이드 아웃을 추천해준다
'''
import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate

ratings = pd.read_csv('../machine_Learning/procect/ratings_small.csv')

reader = Reader(rating_scale=(0.5,5))
data = Dataset.load_from_df(ratings[['userId','movieId','rating']],reader=reader)

svd = SVD(random_state=0)
# cross_validate 모델을 나눠서 교차 검증 , cv=5는 5세트로 나누어서 검증
# valuation = cross_validate(svd,data,measures=['RMSE','MAE'],cv=5,verbose=True)
# print(valuation)

# 학습
trainset = data.build_full_trainset()
svd.fit(trainset)

userId = ratings[ratings['userId'] == 1]
# print(userId)

# (1-userId, 1029-movieId, 3-rating)
print(svd.predict(1,1029,3))
# item - movieId 영화아이디 r_ui -실제 평가 점수, est - 모델의 예측 평가 점수
# 결과값 : user: 1  item: 1029 r_ui = 3.00   est = 2.88   {'was_impossible': False}