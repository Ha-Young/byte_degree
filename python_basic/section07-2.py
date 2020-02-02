# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

class Car:
    """Parent Class"""  # PEP8 원칙으로 적어줘야됨
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    def show(self):
        return "Car Class 'Show Method!'"

class BmwCar(Car):   # Car 상속
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모로부터 물려받은 속성에 값 초기화(부모클래스 생성자)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):   # Car 상속
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모로부터 물려받은 속성에 값 초기화(부모클래스 생성자)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    # 부모랑 같은 이름의 메소드가 있으면 자동 오버라이딩 된다.
    def show(self):
        print(super().show()) # 부모 self가져올 수 있다
        return 'Car Info : %s %s %s' % (self.type, self.color, self.car_name)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)
# 부모꺼에 접근 가능하고 자기꺼도 접근 가능하다.


# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "suv", "black")
model2.show()

# inheritance Info  -> 상속 관계를 보여주는 것
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())

