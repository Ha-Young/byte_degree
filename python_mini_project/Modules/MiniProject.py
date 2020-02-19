# Byte Degree Python Mini Project를 위한 MiniProject클래스 모듈화
# 2020-02-19 구르딩딩(hychoi)

import sqlite3 as db
import datetime
import Modules.Datas as Datas
import os.path

dbFile = './myShop.db'

class MiniProject:
    # 생성자
    def __init__(self):
        self.conn = db.connect(dbFile, isolation_level=None)
        self.cursor = self.conn.cursor()
        self.Data = Datas.DataList

    # 테이블 생성 (product, order)
    def createTables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product_type(type_id INTEGER PRIMARY KEY AUTOINCREMENT, type_name TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product_color(color_id INTEGER PRIMARY KEY AUTOINCREMENT, color_name TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT NOT NULL, product_price INTEGER NOT NULL, type_id INTEGER NOT NULL, color_id INTEGER, FOREIGN KEY(type_id) REFERENCES product_type(type_id), FOREIGN KEY(color_id) REFERENCES product_color(color_id))") 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, order_date TEXT NOT NULL, order_number INTEGER NOT NULL, order_price INTEGER NOT NULL, product_id INTEGER NOT NULL, FOREIGN KEY(product_id) REFERENCES products(id))")
    
    # 상품 종류, 색상 DB 생성
    def initProductTypeColor(self):
        for i in range(0, len(self.Data.productTypeNameList)):
            self.cursor.execute("INSERT INTO product_type('type_name') VALUES(?)", (self.Data.productTypeNameList[i],))
        for i in range(0, len(self.Data.productColorList)):
            self.cursor.execute("INSERT INTO product_color('color_name') VALUES(?)", (self.Data.productColorList[i],))
    
    # 상품 DB 생성
    def insertProduct(self):
        for i in range(0, len(self.Data.productNameList)):
            if (self.Data.productTypeList[i] == 1 or self.Data.productTypeList[i] == 4): # 아우터와 잠옷은 색상종류가 없다.
                self.cursor.execute("INSERT INTO products('product_name', 'product_price', 'type_id') VALUES(?, ?, ?)", (self.Data.productNameList[i], self.Data.productPriceList[i], self.Data.productTypeList[i]))
            else:
                for j in range(0, len(self.Data.productColorIdList)):
                    self.cursor.execute("INSERT INTO products('product_name', 'product_price', 'type_id', 'color_id') VALUES(?, ?, ?, ?)", (self.Data.productNameList[i], self.Data.productPriceList[i], self.Data.productTypeList[i], self.Data.productColorIdList[j]))
    
    # 데이터 세팅
    def initData(self):
        self.initProductTypeColor()
        self.insertProduct()
    
    # 상품 출력
    def printProducts(self, productList):
        print("{:^10}{:^50}{:^20}{:^20}{:^20}".format("id", "name", "price", "type", "color"))
        for i in productList:
            productId = str(i[0])
            productName = str(i[1])
            productPrice = str(i[2])
            productType = str(i[3])
            productColor = str(i[4])
            print("{:^10}{:^50}{:^20}{:^20}{:^20}".format(productId, productName, productPrice, productType, productColor))
    
    # 상품 주문 확인
    def askOrder(self):
        print("1 : 주문하기\n2 : 되돌아가기")
        inputValue = input()
        print()
        if inputValue is "1":
            self.orderProduct()
        elif inputValue is "2":
            pass
        else:
            print("잘못된 명령어를 입력하셨습니다. 초기화면으로 돌아갑니다.")
            print()
            print()

    # 상품 검색
    def searchProduct(self):
        print("1. 상품명으로 검색")
        print("2. 타입별 검색")
        print("3. 컬러별 검색")
        print("4. 되돌아가기")

        inputValue = input()
        print()

        if inputValue is "1":
            print("상품명을 입력해주세요 : ")
            searchProductName = input()
            self.cursor.execute("SELECT P.product_id, P.product_name, P.product_price, T.type_name, C.color_name FROM products P LEFT JOIN product_type T ON P.type_id = T.type_id LEFT JOIN product_color C ON P.color_id = C.color_id WHERE P.product_name = ?", (searchProductName,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)
            
        elif inputValue is "2":
            print("상품 타입을 입력해주세요 (아우터 : 1, 상의 : 2, 하의 : 3, 잠옷 : 4) : ")
            searchProductType = int(input())
            if searchProductType < 1 or searchProductType > 4:
                print("상품 타입을 잘못입력하셨습니다.")
                return
            self.cursor.execute("SELECT P.product_id, P.product_name, P.product_price, T.type_name, C.color_name FROM products P LEFT JOIN product_type T ON P.type_id = T.type_id LEFT JOIN product_color C ON P.color_id = C.color_id WHERE P.type_id = ?", (searchProductType,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)

        elif inputValue is "3":
            print("상품 컬러를 입력해주세요 (회색 : 1, 검은색 : 2, 흰색 : 3) : ")
            searchProductColor = int(input())
            if searchProductColor < 1 or searchProductColor > 3:
                print("상품 컬러를 잘못입력하셨습니다.")
                return
            self.cursor.execute("SELECT P.product_id, P.product_name, P.product_price, T.type_name, C.color_name FROM products P LEFT JOIN product_type T ON P.type_id = T.type_id LEFT JOIN product_color C ON P.color_id = C.color_id WHERE P.color_id = ?", (searchProductColor,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)

        elif inputValue is "4":
            pass
        else:
            print("잘못된 명령어를 입력하셨습니다. 초기화면으로 돌아갑니다")

        print()
        print()
        self.askOrder()
        
    
    # 전체 상품 보기
    def showProduct(self):
        print("전체 상품 목록")
        self.cursor.execute("SELECT P.product_id, P.product_name, P.product_price, T.type_name, C.color_name FROM products P LEFT JOIN product_type T ON P.type_id = T.type_id LEFT JOIN product_color C ON P.color_id = C.color_id")
        allProducts = self.cursor.fetchall()
        self.printProducts(allProducts)

        print()
        print()
        self.askOrder()

    # 구매하기
    def orderProduct(self):
        print("구매하실 상품의 번호와 수량을 입력해주세요")
        print("상품 번호 : ")
        orderProductId = int(input())
        print("수량 : ")
        orderProductNumber = int(input())
        nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("SELECT product_price FROM products WHERE product_id = ?", (orderProductId,))
        orderProductPrice = self.cursor.fetchall()[0][0]
        orderPrice = orderProductNumber * orderProductPrice
        self.cursor.execute("INSERT INTO orders('order_date', 'order_number', 'order_price', 'product_id') VALUES(?, ?, ?, ?)", (nowDate, orderProductNumber, orderPrice, orderProductId))
        print()
        print()

    # 상품 출력
    def printOrders(self, orderList):
        print("{:^20}{:^20}{:^40}{:^20}{:^20}{:^30}".format("order id", "product id", "product name", "price", "number", "order date"))
        for i in orderList:
            ordertId = str(i[0])
            orderDate = str(i[1])
            orderNumber = str(i[2])
            orderPrice = str(i[3])
            productId = str(i[4])
            productName = str(i[5])
            print("{:^20}{:^20}{:^40}{:^20}{:^20}{:^30}".format(ordertId, productId, productName, orderPrice, orderNumber, orderDate))
        print()
        print()

    # 구매 내역 보기
    def showOrder(self):
         print("현재까지의 주문 내역을 확인합니다.")
         self.cursor.execute("SELECT orders.order_id, orders.order_date, orders.order_number, orders.order_price, orders.product_id, products.product_name FROM orders INNER JOIN products ON orders.product_id = products.product_id")
         orderList = self.cursor.fetchall()
         self.printOrders(orderList)
         input("계속하시려면 Enter 키를 눌러주세요")

if __name__ == "__main__":
    pass

