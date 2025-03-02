'''
    함수
'''

# def open_account() :
#     print("새로운 계좌가 생성되었습니다")

# open_account()


# def dopsit(balance, money) :
#     print("입금이 완료되었습니다. 작액은 {0}".format(balance+money))
#     return balance + money

# balance = 0
# balance = dopsit(balance, 1000)
# print(balance)

'''
    가변인자 
    *을 매개변수로 넣어 출력
'''

# def profile(name, age,*language) :
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("김씨",20,"Python","Java","C","C++","C#")
# # #이름 : 파이썬   나이 : 20        Python Java C C++ C# // 결과값
# profile("이씨",25,"Kotlin","Swift")
# # #이름 : 이씨     나이 : 25        Kotlin Swift // 결과값

'''
    지역변수와 전역변수
'''
gun = 10

def checkpoint(soldiers):
    global gun # 전역 변수 gun을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총:{0}".format(gun))

print("전체 총:{0}".format(gun))
checkpoint(2)
print("남은 총:{0}".format(gun))