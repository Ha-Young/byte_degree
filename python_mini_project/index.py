# -*- coding: utf-8 -*-
import sqlite3 as db
import datetime

# ================ 선언부 =================
class MiniProject:
    # 테이블 생성 (product, order)
    def createTables(cursor):
        cursor.execute("CREATE TABLE IF NOT EXSITS product(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT NOT NULL, product_price INTEGER NOT NULL, type TEXT, colorType TEXT)") 
        cursor.execute("CREATE TABLE IF NOT EXSITS order(order_id INTEGER PRIMARY KEY AUTOINCREMENT, order_date TEXT NOT NULL, order_number INTEGER NOT NULL, order_price INTEGER NOT NULL, product_id INTEGER NOT NULL, FOREIGN KEY(product_id) REFERENCE product(id)")
    # 상품 DB 생성
    def insertProduct(cursor):
        productNameList = ['타이탄 체크 자켓', '세미오버 트렌치 코트', '베이직 울 니트', '프리미엄 케시미어 니트', '레이어 티셔츠', '울 슬렉스', '조거벤츠', '스탠다드 후드티', '스탠다드 후드 집업', '디즈니 프린팅 맨투맨', '팽수 파자마 세트', '토이스토리 우디 파자마 세트']
        productPriceList = [120000, 140000, 72000, 110000, 24000, 43000, 54000, 48000, 63000, 47000, 24000, 18000]
        productTypeList = ['아우터', '아우터', '상의', '상의', '상의', '하의', '하의', '상의', '아우터', '상의', '잠옷', '잠옷']
        productColorList = ['Gray', 'Black', 'White']

        for (i in range(0, len(productNameList))):
            if (productTypeList[i] == '아우터' or productTypeList[i] == '잠옷'):
                cursor.execute("INSERT INTO product('product_name', 'product_price', 'type') VALUES(?, ?, ?)", (productNameList[i], productPriceList[i], productTypeList[i]))
            else:
                for (j in range(0, len(productTypeList))):
                    cursor.execute("INSERT INTO product('product_name', 'product_price', 'type', 'colorType') VALUES(?, ?, ?, ?)", (productNameList[i], productPriceList[i], productTypeList[i], productColorList[j]))

    # 상품 검색
    def searchProduct(cursor):
        print("1. 상품명으로 검색")
        print("2. 타입별 검색")
        print("3. 컬러별 검색")
        print("4. 되돌아가기")

        inputValue = input()
        print()

        if inputValue == "1":
            print("상품명을 입력해주세요 : ")
            searchProductName = input()
            pass
        elif inputValue == "2":
            print("상품 타입을 입력해주세요 (아우터, 상의, 하의, 잠옷) : ")
            searchProductType = input()
            pass
        elif inputValue == "3":
            print("상품 컬러를 입력해주세요 (Gray, Black, White) : ")
            searchProductColor = input()
            pass
        elif inputValue == "4":
            continue
        else:
            print("잘못된 명령어를 입력하셨습니다. 초기화면으로 돌아갑니다")
        
    
    # 전체 상품 보기
    def showProduct(cursor):
        print("전체 상품 목록")

    # 구매하기
    def orderProduct(cursor):
        print("구매하실 상품의 번호와 수량을 입력해주세요")
        print("상품 번호 : ")
        orderProductId = input()
        print("수량 : ")
        orderProductNumber = input()

    # 구매 내역 보기
    def showOrder(cursor):
        pass

## 데이터베이스를 연결하는 코드
conn = db.connect('./resource/myShop.db', isolation_level=None)
cursor = conn.cursor()

## 상품과 주문 테이블을 생성하는 코드
MiniProject.createTables(cursor)

## 상품 데이터를 추가하는 코드 
MiniProject.insertProduct(cursor)

## 상품 목록을 표시하는 코드
input("구르딩딩의 홈쇼핑에 오신것을 환영합니다~ Enter 키를 눌러주세요!") # Enter Game Start!
while true:
    print("원하는 기능의 아래 숫자를 입력해주세요")
    print('1. 상품 검색하여 보기')
    print('2. 전체 상품 보기')
    print('3. 바로 구매하기')
    print('4. 현재까지 구매한 내역 보기')
    print('5. 접속 종료하기')

    inputMenu = input()
    print()

    if inputMenu == "1":
        MiniProject.searchProduct(cursor)
        continue
    elif inputMenu == "2":
        MiniProject.showProduct(cursor)
        continue
    elif inputMenu == "3":
        MiniProject.orderProduct(cursor)
        continue
    elif inputMenu == "4":
        MiniProject.showOrder(cursor)
        continue
    elif inputMenu == "5":
        print("구르딩딩의 홈쇼핑을 이용해주셔서 감사합니다. 다음에 또 방문해주세요~")
        break
    else:
        print("잘못된 명령어를 입력하셨습니다.")
        continue
