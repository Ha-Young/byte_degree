# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 (모든 것들은 네임스페이스를 가지고 있다 (int float string objcect... 모두 다))
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재

# 선언
class 클래스명:
    #속성
    #함수
    #함수
    #함수...
    pass

# 예제11
class UserInfo:
    #속성, 메소드
    def __init__(self, name):
        self.name = name
        print("초기화")

    def user_info_p(self):
        print("Name : %s" % self.name)

user1 = UserInfo("Choi")
user1.user_info_p()
user2 = UserInfo("Kim")
user2.user_info_p()
print(user1.name)
print(user2.name)

# 네임스페이스 -> 각각 인스턴스가 가지고 있는 영역은 다르다.
# 그래서 각각 인스턴스가 가지고 있는 값은 다르고 각기 다른 저장공간을 가지고 있는데,
# 그것이 바로 네임스페이스.

# 예제2
class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

self_test = SelfTest()
# self_test.function1() # self 매개변수가 없으므로 호출불가 애러남.
SelfTest.function1()  # self를 매개변수로 넘겨주지 않으면 클래스 메소드로 클래스에서 호출가능하다.
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수(공유) -> stock_num이 여기서 나온다. 클래스 맴버변수

print(user1.stock_num) # 자기 네임스페이스에 없으면 클래스 네임스페이스에서 찾아온다.

del user1 # __del__ 함수가 작동되고 인스턴스 메모리에서 제거된다. (네임스페이스 제거)

print(user2.stock_num)
print(user3.stock_num)

# 예제4
class Car:
    """Parent Class"""
    instanceNum = 0
    def __init__(self):
        print("Car instance Cunstructor...!")
        Car.instanceNum += 1
    
    def __del__(self):
        print("Car instance Destoyed...!")
        Car.instanceNum -= 1
    

car = Car()

car.instanceNum += 5  # 클래스꺼에서 자기꺼로 변경되는 듯.
car.hoho = 5

print(Car.instanceNum)
print(car.instanceNum)  
print(car.hoho)
car2 = Car()

print(Car.instanceNum)
print(car2.instanceNum)