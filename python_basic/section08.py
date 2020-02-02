# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)

#from 폴더 import 클래스
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci("hoho").title)

# 사용2(클래스) -> 메모리 사용 많이하여 권장X
from pkg.fibonacci import *   # 전부 가져온다

Fibonacci.fib(600)

print("ex2 : ", Fibonacci.fib2(600))
print("ex2 : ", Fibonacci("use2").title)

# 사용3(클래스) -> 권장. Alias 이용
from pkg.fibonacci import Fibonacci as Fib

Fib.fib(1000)

print("ex3 : ", Fib.fib2(1400))
print("ex3 : ", Fib("use3").title)

# 사용4(함수)
#import 파일   -> 그 파일안에 있는 모든 것을 가져온다
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수) -> 권장.
# from 파일 import 함수 as 요약명
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins   # 기본으로 가지고 있는 것. 디폴트로 가져오게 되어있다
p.prt1()
p.prt2()
print(dir(builtins))
