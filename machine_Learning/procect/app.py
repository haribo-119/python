'''
    영화 추천 웹사이트 #1
'''
import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

st.set_page_config(layout='wide')

movie = Movie()
tmdb = TMDb()
tmdb.api_key ='input api key'

'''
    영화 추천 웹사이트 #2
'''
def get_recommendations(title):
    # 1) 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    
    # 2) 코사인 유사도 매트릭스 (consine_sim)에서 idx 에 해당하는 데이터를 (idx,유사도) 형태로 얻기
    
    # 3) 코사인 유사도 기준으로 내림차순 정렬
    
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    
    # 4) 추천 영화 목록 10개의 인덱스 정보 추출
    
    # 5) 인덱스 정보를 통해 영화 제목 추출
    return

movies = pickle.load(open('..\machine_Learning\procect\movies.pickle','rb'))
cosine_sim = pickle.load(open('..\machine_Learning\procect\cosine_sim.pickle','rb'))

st.header("hlep_movies_choice")

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like',movie_list)
if st.button('Recommend'):
    images, title = get_recommendations(title)
    pass