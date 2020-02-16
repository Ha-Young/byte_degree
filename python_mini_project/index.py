# -*- coding: utf-8 -*-
import sqlite3 as db
import datetime

# ================ 선언부 =================
class MiniProject:
    productNameList = ['타이탄 체크 자켓', '세미오버 트렌치 코트', '베이직 울 니트', '프리미엄 케시미어 니트', '레이어 티셔츠', '울 슬렉스', '조거벤츠', '스탠다드 후드티', '스탠다드 후드 집업', '디즈니 프린팅 맨투맨', '팽수 파자마 세트', '토이스토리 우디 파자마 세트']
    productPriceList = [120000, 140000, 72000, 110000, 24000, 43000, 54000, 48000, 63000, 47000, 24000, 18000]
    productTypeList = ['아우터', '아우터', '상의', '상의', '상의', '하의', '하의', '상의', '아우터', '상의', '잠옷', '잠옷']
    productColorList = ['Gray', 'Black', 'White']

    def __init__(self):
        self.conn = db.connect('./myShop.db', isolation_level=None)
        self.cursor = self.conn.cursor()
    # 테이블 생성 (product, order)
    def createTables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT NOT NULL, product_price INTEGER NOT NULL, type TEXT, colorType TEXT)") 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, order_date TEXT NOT NULL, order_number INTEGER NOT NULL, order_price INTEGER NOT NULL, product_id INTEGER NOT NULL, FOREIGN KEY(product_id) REFERENCES products(id))")
    # 상품 DB 생성
    def insertProduct(self):
        for i in range(0, len(self.productNameList)):
            if (self.productTypeList[i] == '아우터' or self.productTypeList[i] == '잠옷'):
                self.cursor.execute("INSERT INTO products('product_name', 'product_price', 'type') VALUES(?, ?, ?)", (self.productNameList[i], self.productPriceList[i], self.productTypeList[i]))
            else:
                for j in range(0, len(self.productColorList)):
                    self.cursor.execute("INSERT INTO products('product_name', 'product_price', 'type', 'colorType') VALUES(?, ?, ?, ?)", (self.productNameList[i], self.productPriceList[i], self.productTypeList[i], self.productColorList[j]))

    # 상품 출력
    def printProducts(self, productList):
        print("{:^10}{:^50}{:^20}{:^20}{:^20}".format("number", "name", "price", "type", "color"))
        for i in productList:
            productId = str(i[0])
            productName = str(i[1])
            productPrice = str(i[2])
            productType = str(i[3])
            productColor = str(i[4])
            print("{:^10}{:^50}{:^20}{:^20}{:^20}".format(productId, productName, productPrice, productType, productColor))

    # 상품 검색
    def searchProduct(self):
        print("1. 상품명으로 검색")
        print("2. 타입별 검색")
        print("3. 컬러별 검색")
        print("4. 되돌아가기")

        inputValue = input()
        print()

        if inputValue == "1":
            print("상품명을 입력해주세요 : ")
            searchProductName = input()
            self.cursor.execute("SELECT * FROM products WHERE product_name = ?", (searchProductName,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)
            
        elif inputValue == "2":
            print("상품 타입을 입력해주세요 (아우터, 상의, 하의, 잠옷) : ")
            searchProductType = input()
            if searchProductType != "아우터" and searchProductType != "상의" and searchProductType != "하의" and searchProductType != "잠옷":
                print("상품 타입을 잘못입력하셨습니다.")
                return
            self.cursor.execute("SELECT * FROM products WHERE type = ?", (searchProductType,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)

        elif inputValue == "3":
            print("상품 컬러를 입력해주세요 (Gray, Black, White) : ")
            searchProductColor = input()
            if searchProductColor != "Gray" or searchProductColor != "Black" or searchProductColor != "White":
                print("상품 컬러를 잘못입력하셨습니다.")
                return
            self.cursor.execute("SELECT * FROM products WHERE colorType = ?", (searchProductColor,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)

        elif inputValue == "4":
            pass
        else:
            print("잘못된 명령어를 입력하셨습니다. 초기화면으로 돌아갑니다")
        print()
        print()
    
    # 전체 상품 보기
    def showProduct(self):
        print("전체 상품 목록")
        self.cursor.execute("SELECT * FROM products")
        allProducts = self.cursor.fetchall()
        self.printProducts(allProducts)
        print()
        print()

    # 구매하기
    def orderProduct(self):
        print("구매하실 상품의 번호와 수량을 입력해주세요")
        print("상품 번호 : ")
        orderProductId = input()
        print("수량 : ")
        orderProductNumber = input()

    # 구매 내역 보기
    def showOrder(self):
        pass

## 데이터베이스를 연결하는 코드
miniProject = MiniProject()

## 상품과 주문 테이블을 생성하는 코드
miniProject.createTables()

## 상품 데이터를 추가하는 코드 
miniProject.insertProduct()

## 상품 목록을 표시하는 코드
input("구르딩딩의 홈쇼핑에 오신것을 환영합니다~ Enter 키를 눌러주세요!")    # Enter Game Start!

while True:
    print("원하는 기능의 아래 숫자를 입력해주세요")
    print('1. 상품 검색하여 보기')
    print('2. 전체 상품 보기')
    print('3. 바로 구매하기')
    print('4. 현재까지 구매한 내역 보기')
    print('5. 접속 종료하기')

    inputMenu = input()
    print()

    if inputMenu == "1":
        miniProject.searchProduct()
        continue
    elif inputMenu == "2":
        miniProject.showProduct()
        continue
    elif inputMenu == "3":
        miniProject.orderProduct()
        continue
    elif inputMenu == "4":
        miniProject.showOrder()
        continue
    elif inputMenu == "5":
        print("구르딩딩의 홈쇼핑을 이용해주셔서 감사합니다. 다음에 또 방문해주세요~")
        break
    else:
        print("잘못된 명령어를 입력하셨습니다.")
        continue
