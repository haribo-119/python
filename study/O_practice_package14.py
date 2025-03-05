'''
    패키지
'''

# 클래스나, 함수는 직접 임포트 할 수 없다
import travel.thailand # thailand은 모듈이나 패키지만 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# # 클래스나 함수를 가져올때 사용 방법
from travel.thailand import ThailandPackage
trip_to =  ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietanmPackage()
trip_to.detail()


'''
    __all__
'''
# from random import * 처럼 사용 가능
# 조건 __init__.py 파일에 
# __all__ ["vietnam"] 을 기재
from travel import *
trip_to = vietnam.VietanmPackage()
trip_to.detail() 

'''
    모듈 위치 확인 
    랜덤 모듈의 같은 위치에 새로운 모듈을 넣어 사용가능
'''
import inspect
import random
from travel import*
print(inspect.getfile(random))
print(inspect.getfile(thailand))


'''
  pip install
'''
# 터미널에서
# pip list  - 현재 설치한 패키지 리스트
# pip show beautifulsoup4 - 간단한 설명
# pip install --upgrade 패키지명 - 설치한 패키지 업그레이드 
# pip uninstall 패키지명 - 삭제