'''
    클래스
'''

'''
    클래스 [사용전]
'''
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음

# name = "마린"
# hp = 40
# damage = 5
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쓸 수 있는데, 일반 모드 / 시즈 모드.

# tank_name ="탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage) :
#     print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))

# # tank2_name ="탱크"
# # tank2_hp = 150
# # tank2_damage = 35
# # print("{0} 유닛이 생성되었습니다.".format(tank_name))
# # print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# # def attack(name,location,damage) :
# #     print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))

# ## 매번 탱크를 생산하기 위해 만들 수는 없음


# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# # attack(tank2_name,"1시",tank2_damage)


'''
    클래스 [사용]
'''
class Unit :
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))


# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

'''
    __init__ // 파이썬에서 사용되는 생성자
'''

'''
 맴버변수 // self.name = name, self.hp = hp, self.damage = damage
         // 클래스 내에 정의된 변수
'''

# # 레이스 생성
# wraith1 = Unit("레이스",80,5)
# print("유닛 이름:{0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))
# # 외부에서 맵버변수를 가져옴

'''
    객체에 변수 추가
'''

# wraith2 = Unit("레이스2","80","5")
# wraith2.clocking = True #Unit에는 없는 변수 clocking, 파이썬을 추가 가능
# if wraith2.clocking == True:
#     print("{0}는 현재 크로킹 상태 입니다".format(wraith2.name))

'''
    메소드
'''
class AttackUnit :
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 전국을 공격합니다.[공격력{2}]"
              .format(self.name,location,self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))    
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어벳",50,16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)


