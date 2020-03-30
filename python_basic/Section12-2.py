# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('./resource/database.db') # DB커넥트

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# # 1개 로우 선택
# print('One -> \n', c.fetchone())

# # 지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# # 전체 로우 선택
# print('All -> \n', c.fetchall())

# print(c.fetchall()) # 아무것도 없다 (커서가 끝이라서)

print()

# # 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrive1 > ', row)

# # 순회2
# for row in c.fetchall():
#     print('retrive2 > ', row)

# # 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrive3 > ', row)

# WHERE Retrive1
param1 = (3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrive2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2', c.fetchone())
print('param2', c.fetchall())

# WHERE Retrive3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id" : 5})
print('param3', c.fetchone())
print('param3', c.fetchall())

# WHERE Retrive4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

# WHERE Retrive5
c.execute("SELECT * FROM users WHERE id IN(%d,%d)" % (3, 4))
print('param5', c.fetchall())

# WHERE Retrive6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1":2, "id2":5})
print('param6', c.fetchall())

# Dump 출력
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')








 