# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# key, value (Json) -> MongoDB
# 선언
a = {'name' : 'Kim', 'Phone' : '010-7777-7777', 'birth' : '921028', 'age' : 29}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'array': [1, 2, 3,4]}
d = {'tuple': (1, 5, 3,2)}
print(a['name'])
print(b[1])
print(c['array'])
print(d['tuple'])

print(a.get('name'))
print(a.get('address'))
print(c['array'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3, 4]
a['rank2'] = (1, 4, 2,)
print(a)

# keys, values, items // item : key,value 모두 다

print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())

print(a.items())

print(2 in b)

# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set(1, 4, 5, 6, 6)

print(type(a))
print(c)


for i in c:
    print(i)