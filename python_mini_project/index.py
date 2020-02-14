# -*- coding: utf-8 -*-
import sqlite3 as db

## 데이터베이스를 연결하는 코드
conn = db.connect('./resource/myShop.db', isolation_level=None)
cursor = conn.cursor()

## 상품과 주문 테이블을 생성하는 코드
cursor.execute("CREATE TABLE IF NOT EXSITS product(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT NOT NULL, product_price INTEGER NOT NULL, type TEXT)") 
cursor.execute("CREATE TABLE IF NOT EXSITS order(order_id INTEGER PRIMARY KEY AUTOINCREMENT, order_date TEXT NOT NULL, order_price INTEGER NOT NULL, product_id INTEGER NOT NULL, FOREIGN KEY(product_id) REFERENCE product(id)")

## 상품 데이터를 추가하는 코드
cursor.execute("INSERT INTO product ")

## 상품 목록을 표시하는 코드

print('')
print("구매하실 상품의 번호를 입력해주세요: ")


## 상품 번호와 주문 수량을 입력받는 코드
print('')
print("구매할 수량을 입력해주세요: ")


## 주문 데이터를 db에 추가하는 코드
# c.execute("INSERT INTO ...

## 현재까지 주문 내역을 출력하는 코드
print('')
print("현재까지 구매한 내역 보기")
print('')