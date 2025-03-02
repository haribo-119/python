station = "사당"

print(station+"행 열차가 들어오고 있습니다")

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기
print(10%3) # 1 몫 구하기
print(5//3) # 1 몫 구하기
print(10//3) # 2 몫 구하기

print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 4*4 =16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 3
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) +1) # 1 ~ 10 이하의 임의 값 생성

print(randrange(1, 46)) # 1 ~ 46  미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

print(randint(1,31))