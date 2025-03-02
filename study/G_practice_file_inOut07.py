'''
    파일 입출력
'''
# # 쓰기
# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0",file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()

# # 이미 작성된 파일에 이어쓰기
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") #쓰기(W)에서는 자동으로 줄바꿈을 해줬음
# #\n 으로 줄바꿈이 필요
# score_file.close()

# # 모두 읽어 오기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# # 한줄씩 읽어오기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="") # 한줄씩 읽어오기, 커서는 아래로이동
# print(score_file.readline(),end="") # 한줄씩 읽어오기, 커서는 아래로이동
# score_file.close()

# # 반복문 한줄씩 가져오기
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

# 리스트로 읽어오기
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()