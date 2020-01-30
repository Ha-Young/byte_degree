# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_str1))
print(type(v_dict))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

print(type(big_int1))


# 형변환
# int, float, complex(복소수)
f1 = 3.5
print(int(f1))
print(float(i2))
print(complex(3))
print(bool(3))
print(bool(0))

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))
print(math.floor(5.1))

# Raw String - escape 적용X
raw_s1 = r'c:\Program\Test\Bin'
print(raw_s1)

# 멀티라인
multi = \
""" 
문자열 

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc "
str_03 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print((str_o2 + str_03) * 2)
print('a' in str_o4)
print('' in str_o4)
print('z' not in str_o4)
print(str_o4.__contains__('z'))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'origin'

print(list(reversed(b)).__str__())
print(str(a))


print() 
print(a[0:3])
print(a[0:4])
print(a[0:len(a)-1])
print(a[:])
print(b[0:6:2])
print(b[1:-2])
print(b[::-1])
