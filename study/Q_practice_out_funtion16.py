'''
    외장 함수
'''
# list of python modules 검색

# glob :  경로 내의 폴터 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든파일

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder) :
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다다")
# else :
#     os.makedirs(folder) # 폴더 생성
#     print(folder,"폴더를 생성하였습니다.")

# import os
# print(os.listdir())

'''
    time : 시간 관련 함수
'''
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만나지 100일은", today + td) # 오늘부터 100일 후