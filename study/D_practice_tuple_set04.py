# 듀플
# 내용 변경이나, 추가할 수 없음
# 속도가 [리스트] 보다 빠름

menu =("돈까스","치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생성까스") # 에러

# name ="파이썬"
# age = 20
# hobby ="코딩"
# print(name, age, hobby)

(name, age, hobby) = ("파이썬",20,"코딩")
print(name, age, hobby)

# 집합 (set)
# 중복 X , 순서가 없음
my_set = {1,2,3,3,3,3}
print(my_set) # 중복을 허용하지 않음

java = {"해","달","하늘"} # 리스트
python = set(["해","별"])

# 교집합, java와 python에 공통으로 해당하는 단어
print(java & python) # 해
print(java.intersection(python)) # 해

# 합집합 
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 추가, set 추가
python.add("구름")
print(python)

# 제거
java.remove("달")
print(java)

# 자료 구조 변경
menu  = {"커피","우유","주스"} # { } 집힙 set이다
print(menu,type(menu)) # {'주스', '우유', '커피'} <class 'set'>

menu = list(menu)
print(menu,type(menu)) # ['주스', '우유', '커피'] <class 'list'>

menu = tuple(menu)
print(menu,type(menu)) # ('주스', '우유', '커피') <class 'tuple'>