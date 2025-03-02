'''
 if문
'''

# # weather = input("오늘 날씨는 어때요?")

# # # if 조건 :
# # #     실행 명령문

# # if weather == "비" or weather == "눈":
# #     print("우산을 챙기세요")
# # elif weather == "미세먼지" :
# #     print("마스크를 챙기세요")
# # else :
# #     print("준비물 필요 없어요")

# temp = int(input("기온은 어떄요?"))

# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <=temp and temp <30 :
#     print("괜찮은 날씨에요")
# elif 0 <=  temp and temp <10 :
#      print("외투를 챙기세요")
# else :
#     print("너무 추워요. 나가지 마세요")


'''
    for문
'''

# for waiting_no in range(5) : # 0,1,2,3,4
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1,6) : # 1,2,3,4,5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨","토르","그루트"]

# for customer in starbucks :
#     print("{0}, 커피가 준비되었습니다".format(customer))



'''
    while문
'''  

# customer = "토르"
# index = 5

# while index >= 1 :
#     print("{0}, 커피기 준비되었습니다. {1}번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

'''
    contiue, break
'''

# absent = [1,2,5] # 결석
# no_book =[7]
# for student in range(1,11) : # 1,2,3,4,5,6,7,8,9,10
#     if student in absent :
#         continue
#     elif student in no_book :
#         print("오늘 수업 여기까지.{0}번".format(student))
#         break 
#     print("{0}, 책을 읽어봐".format(student))

'''
    한 줄 for문
'''

# # 출석번호 1 2 3 4 5 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 105
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# # 학생 이름을 길이로 변환
# students =["man","k","weather"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변경
students =["man","k","weather"]
students =[i.upper() for i in students]
print(students)