# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]
f = [10, "asdf", True]

# 인덱싱
print(e[2][1])
print(e[-1][-2])
print(f[2])

# 슬라이싱
print(f[0:2])
print(e[0:len(e)])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')
print(str(c) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:3] = [100, 1000, 1000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[1:3]
print(c)

print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y = y.__add__([5])
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2)
y.remove(5)
print(y)
popV = y.pop()
print(y)
print(popV)
ex = [88, 77]
y.extend(ex)
print(y)
y.append(ex)
print(y)

# 삭제 : del, remove, pop
# 삽입 : [index], append <-> extend, add

# ////////////////////////////////////////////////

# 튜플 (순서o, 중복o, 수정x, 삭제x)
a = ();
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
print(d)
print(c[2])
print(d[2][2])

print(d[2:])
print(d[2][0:6])

print(c + d)

# 튜플 함수
z = (5, 2, 1, 3, 4, 1)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))