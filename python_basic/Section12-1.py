# Section12
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime as dt
#  삽입 날짜 생성
now = dt.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite.sqlite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit, Rollback
# commit : 반영, rollback : 되돌리기
# sqlite database borwser portable 설치하기
conn = sqlite3.connect('./resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))
print(dir(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, \
    email TEXT, phone TEXT, website TEXT, regdate TEXT)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-9999-9999', \
   'Kim.com', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",
(2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@gmail.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate)\
    VALUES (?,?,?,?,?,?)", userList);

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)
