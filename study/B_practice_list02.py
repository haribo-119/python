# # 리스트 []

# # 지하철 칸별로 10명, 20명, 30명
# # subway1 = 10
# # subway2 = 20
# # subway3 = 30

# subway = [10,20,30]

# print(subway)

# subway = ["별","바람","하늘"]

# print(subway)

# # 바람이 몇 번째 칸에 타고 있는가?
# print(subway.index("바람"))

# # 달이 다음 정류장에 탈 경우
# subway.append("달")
# print(subway)

# # 밤을 별과 바람 사이에 넣기
# subway.insert(1, "밤")
# print(subway)

# # 뒤에서 한병씩 꺼냄
# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명있는지 확인
# subway.append("별")
# print(subway)
# print(subway.count("별"))

# # 정렬도 가능
# num_list = [5,2,1,3,4]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기 
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,1,3,4]
# mix_list = ["별",1,"바람",2,True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 딕셔너리  사전
# cabinet = {3:"별",100:"달"}
# # print(cabinet[3])
# # print(cabinet[100])
# # print(cabinet.get(3))

# # # print(cabinet[5]) # 에러
# # # print(cabinet.get(5)) # NONE 출력

# print(3 in cabinet) # key값 in 변수 # 결과값은 true, false

cabinet = {"A":"별","B":"달"}

# 추가
cabinet["c"] = "하늘"
print(cabinet)

# 변경
cabinet["A"] ="우주"
print(cabinet)

# 삭제
del cabinet["B"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 삭제
cabinet.clear()
print(cabinet.clear())