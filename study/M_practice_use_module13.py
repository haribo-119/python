'''
    모듈
'''
# 모듈은 내가 사용하려는 파일과 같은 경로에 있어야 한다
# 또는 파이썬 라이브러이에 모인 폴더에 있어야 사용가능


# 모듈 사용 조건
# import module  
# module.price(3) # 3명이서 영화 보러 갔을 때 가격
# module.price_morinig(4) # 4명이서 조조 할인 영화 보러 갔을 때
# module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때


# 모듈 별명 
# import module as mv 
# mv.price(3)
# mv.price_morinig(4)
# mv.price_soldier(5)

# from 모듈듈 - 함수만 호출 가능
from module import * # *아스타 대신 필요한 함수만 넣어 호출 가능
# from radom import * 와 같다
price(3)
price_morinig(4)
price_soldier(5)


from module import price as price_morinig
# price 함수를 호출, 별명은 price_morinig으로 사용

