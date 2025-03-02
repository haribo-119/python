# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : "  + jumin[0:2])

# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " +  jumin[-7:])

'''
문자열 함수
'''

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) 
# # python의 첫번째 문자가 대문자인가? 맞으면 true, 틀리면 false

# print(len(python)) # 문자열의 길이
# print(python.replace("Python","Java")) 
# # Python is Amazing -> Java is Amazing

# index = python.index("n")
# print(index)
# index = python.index("n",index+1)
# # 두번째 "n" 을 찾아 준다
# print(index)

# print(python.find("Java")) # 찾는 값이 없으면 -1을 반환
# # print(python.index("Java")) # 오류 발생

# print(python.count("n")) # n의 개수를 세어줌

'''
문자열 포맷
'''
# # 방법1
# print("나는 %d살 입니다." % 20) # 정수
# print("나는 %s을 좋아해요." % "파이썬") #문자열,
# print("Apple 은 %c로 시작해요." % "A") # 문자, %c 캐릭터로 "A"에서 첫글자만 가져온다

# print("나는 %s살 입니다." % 20) # %s를 사용하면 정수, 문자열 상관없음
# print("나는 %s색과 %s색을 좋아해요." % ("파란","빨강"))

# # 방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨강"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨강"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨강"))

# # 방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20, color="빨강"))
# print("나는 {color}살이며, {age}색을 좋아해요.".format(age =20, color="빨강"))

# # 방법4 (v3.6 이상~)
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

'''
탈출문자
'''
# print("백문이 불여일견 \n백견이 불여일타") # \n 줄바꿈
# print("저는 '나도코딩'입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")

# # print("C:\User\Nadocoding\Desktop\Pythonworkspace") #에러
# print("C:\\User\\Nadocoding\\Desktop\\Pythonworkspace")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine") # PineApple

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")