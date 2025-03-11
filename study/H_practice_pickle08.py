'''
    pickle
'''

import pickle

# #데이터 저장
# profile_file = open("profile.pickle","wb") 
# # wb에서 w 쓰기, b는 바이너리를 의미 (pickle은 바이너리가 필요)

# profile ={"이름":"사용자","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile에 있는 정보를 file에 저장

# profile_file.close()

# # 데이터 가져오기
# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

'''
    with
'''
# with을 사용하면 자동으로 close() 닫아준다
with open("profile.pickle","rb") as profile_file :
    print(pickle.load(profile_file))


