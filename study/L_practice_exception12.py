'''
    예외처리
'''
# try:
#         print("나누기 전용 계산기입니다.")
#         nums = []
#         nums.append(int(input("첫 번째 숫자를 입력하새요 : ")))
#         nums.append(int(input("두 번째 숫자를 입력하새요 : ")))
#         # nums.append(int(nums[0]/nums[1]))
#         print("{0} / {1} = {2}".format(nums[0],nums[1], nums[2]))
# except ValueError:
#         print("에러! 잘못된 값을 입력하였씁니다.")
# except ZeroDivisionError as err :
#         print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다")
#     print(err)

'''
    에러 발생시키기
'''
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # !1) 10값을 넘게 입력하면 에러를 발생
#     print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))
# except ValueError : # 2) 발생한 에러 처리
#     print("잘못된 값을 입력하였습니다. 한 자리 수만 입력하세요.")

'''
    사용자 정의 에러
'''

class BinNumberError(Exception) :
        # 2)사용자 정의 에러, 1)의 "입력값 : {0},{1}".format(num1,num2) 받아서 3)반환
        def __init__ (self,msg):
             self.msg = msg
        def __str__ (self) :
             return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BinNumberError("입력값 : {0},{1}".format(num1,num2)) # !1) 사용자 정의 에러
    print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))
except ValueError : 
    print("잘못된 값을 입력하였습니다. 한 자리 수만 입력하세요.")
except BinNumberError as err : 
    print("에러가 발생하였습니다. 한 자리 수만 입력하세요.")
    print(err) # 3) 발생한 에러 처리  
finally: # 무조건 출력
         print("계산기를 이용해 주셔서 감사합니다.")

'''
    사용자 정의 에러 결과 값    
'''
# 첫 번째 숫자를 입력하세요 : 10
# 첫 번째 숫자를 입력하세요 : 5
# 에러가 발생하였습니다. 한 자리 수만 입력하세요.
# 입력값 : 10,5