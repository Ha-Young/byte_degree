# decorator에 대해 학습

def decorator_function(original_function):
    def wrapper_function():
        print("{} 함수가 호출되기전 입니다.".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display_1():
    print("display_1 함수가 실행되었습니다.")

def display_2():
    print("display_2 함수가 실행되었습니다")

display_1 = decorator_function(display_1)
display_2 = decorator_function(display_2)

display_1()
print()
display_2()

print("\n##############\n")

# 간략화 "@" 심볼과 데코레이터 함수 이름을 붙여 사용

def decorator_function_(original_function):
    def wrapper_function():
        print("{} 함수가 호출되기전 입니다.".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function_
def display_1_():
    print("display_1 함수가 실행되었습니다.")

@decorator_function_
def display_2_():
    print("display_2 함수가 실행되었습니다")

# display_1 = decorator_function(display_1)
# display_2 = decorator_function(display_2)

display_1_()
print()
display_2_()

print("\n##############\n")

def decorator_function__(original_function):
    def wrapper_function(*args, **kwargs):
        print("{} 함수가 호출되기전 입니다.".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function__
def display():
    print("display 함수가 실행되었습니다.")

@decorator_function__
def display_info(name, age):
    print("display_info({}, {}) 함수가 실행되었습니다.".format(name, age))

display()
print()
display_info("John", 25)

print("\n##############\n")

# 클래스 형식 데코레이터
class DecoratorClass:  #1
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass  #2
def display_():
    print('display 함수가 실행됐습니다.')


@DecoratorClass  #3
def display_info_(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_()
print()
display_info_('John', 25)

print("\n##############\n")

# 일반적으로 데코레이터는 로그를 남기거나 
# 유저의 로그인 상태등을 확인하여 로그인 상태가 아니면 
# 로그인 페이지로 리더랙트(redirect)하기 위해서 많이 사용됩니다. 
# 또한 프로그램의 성능을 테스트하기 위해서도 많이 쓰입니다. 
# 리눅스나 유닉스 서버 관리자는 스크립트가 실행되는 시간을 측정하기 위해서 
# 다음과 같은 date와 time 명령어를 많이 사용합니다.

# 데코레이터로 만든 로깅 기능

# functools 모듈의 wraps 데코레이터는 데코레이터 호출순서, 스택에 관계없이 original_function을 찾아준다.
from functools import wraps
import datetime
import time

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        print("my_logger")
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] 실행 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        logging.info("[{}] 실행된 총 시간: {} 초".format(timestamp, t2))
        return result

    return wrapper

def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        print("my_timer")
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print("{} 함수가 실행된 총 시간: {} 초".format(original_function.__name__, t2))
        return result

    return wrapper
    

@my_timer
@my_logger
def display_info__(name, age):
    time.sleep(1)
    print("displayinfo__({}, {}) 함수가 실행되었습니다.".format(name,age))
    
display_info__("HaYoung", 29)

