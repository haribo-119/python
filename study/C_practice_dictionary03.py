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