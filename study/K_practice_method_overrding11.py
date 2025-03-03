'''
    메서드 오버라이딩 전
'''
# # 일반 유닛 
# class Unit :
#     def __init__(self,name,hp,speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self,location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"
#               .format(self.name,location,self.speed))

# # 공격 유닛
# class AttackUnit(Unit): 
#     def __init__(self,name,hp,damage,speed):
#         Unit.__init__(self,name,hp,speed) 
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 전국을 공격합니다.[공격력{2}]"
#               .format(self.name,location,self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))    
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 날 수 있는 기능을 가진 클래스 
# class Flyable :
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"
#               .format(name,location,self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit,Flyable): 
#     # 다중 상속 class의 AttackUnit과 Flyable 상속
#     def __init__(self,name,hp,damage,flying_speed) :
#       AttackUnit.__init__(self,name,hp,0,damage) # 0은 지상 스피드
#       Flyable.__init__(self,flying_speed)


# #벌처 유닛 생성
# vulture = AttackUnit("벌처",80,10,20)

# #배틀크루저 생성
# battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)


#문제점 : 지상 유닛일땐 move를 공중 유닛은 fly를 사용 
# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")


'''
    메서드 오버라이딩 후
'''
# 일반 유닛 
class Unit :
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"
              .format(self.name,location,self.speed))

# 공격 유닛
class AttackUnit(Unit): 
    def __init__(self,name,hp,damage,speed):
        Unit.__init__(self,name,hp,speed) 
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

# 날 수 있는 기능을 가진 클래스 
class Flyable :
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"
              .format(name,location,self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable): 
    # 다중 상속 class의 AttackUnit과 Flyable 상속
    def __init__(self,name,hp,damage,flying_speed) :
      AttackUnit.__init__(self,name,hp,0,damage) # 0은 지상 스피드
      Flyable.__init__(self,flying_speed)
    
    def move(self,location): # ! Unit 클래스의 move 메서드 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

#벌처 유닛 생성
vulture = AttackUnit("벌처",80,10,20)

#배틀크루저 생성
battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

# move 메서드 생성 
vulture.move("11시")
battlecruiser.move("9시")

'''
    pass
    -- 에러없이 그냥 다음으로 넘어간다
'''
# #건물 
# class BuildingUnit(Unit):
#     def __init__(self,name,hp,location):
#         pass #! 패스는 아무것도 안하고 넘어간다

# # 건물 생성
# supply_depot = BuildingUnit("서블라이 디폿",500,"7시")    

'''
    super
    1) super()는 다중상속일 경우, FlyableAttackUnit(AttackUnit,Flyable)
        AttackUnit의 정보만 가져옴
    2)  다중 상속일 경우, 명시적으로 초기화 해줘야 한다         
'''
#건물 
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        #Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) 
        # ! super()를 사용하면, self정보는 뺴도됨
        self.location = location