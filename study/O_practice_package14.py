'''
    패키지
'''

# 클래스나, 함수는 직접 임포트 할 수 없다
import travel.thailand # thailand은 모듈이나 패키지만 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# 클래스나 함수를 가져올때 사용 방법
from travel.thailand import ThailandPackage
trip_to =  ThailandPackage()
trip_to.detail()