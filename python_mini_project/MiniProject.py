# Byte Degree Python Mini Project를 위한 MiniProject클래스 모듈화
# 2020-02-19 구르딩딩(hychoi)

import sqlite3 as db
import datetime

class MiniProject:
    # 필요 데이터 리스트
    productNameList = ['Titan Check Jaket', 'Semiover Tranch Coat', 'Basic Wool Knit', 'Premium Cashmier Knit', 'Bent Layered T-Shirt', 'Wool Slacks', 'Jogger Pants', 'Standard Hood T-Shirt', 'Standard Hood Zipup', 'Printing Sweatshirt', 'Peng-Su Pajama Set', 'Toystory Woodie Pajama Set']
    productPriceList = [120000, 140000, 72000, 110000, 24000, 43000, 54000, 48000, 63000, 47000, 24000, 18000]
    productTypeList = [1, 1, 2, 2, 2, 3, 3, 2, 1, 2, 4, 4]
    productTypeNameList = ['Outer', 'Top', 'Bottom', 'Pajama']
    productColorList = ['Gray', 'Black', 'White']
    productColorIdList = [1, 2, 3]

    # 생성자
    def __init__(self):
        self.conn = db.connect('./myShop.db', isolation_level=None)
        self.cursor = self.conn.cursor()

    # 테이블 생성 (product, order)
    def createTables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product_type(type_id INTEGER PRIMARY KEY AUTOINCREMENT, type_name TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product_color(color_id INTEGER PRIMARY KEY AUTOINCREMENT, color_name TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT NOT NULL, product_price INTEGER NOT NULL, type_id INTEGER NOT NULL, color_id INTEGER, FOREIGN KEY(type_id) REFERENCES product_type(type_id), FOREIGN KEY(color_id) REFERENCES product_color(color_id))") 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, order_date TEXT NOT NULL, order_number INTEGER NOT NULL, order_price INTEGER NOT NULL, product_id INTEGER NOT NULL, FOREIGN KEY(product_id) REFERENCES products(id))")
    
    # 상품 종류, 색상 DB 생성
    def initProductTypeColor(self):
        for i in range(1, len(self.productTypeNameList) + 1):
            self.cursor.execute("INSERT INTO product_type('type_id', 'type_name') VALUES(?, ?)", (i, self.productTypeNameList[i-1]))
        for i in range(1, len(self.productColorList) + 1):
            self.cursor.execute("INSERT INTO product_color('color_id', 'color_name') VALUES(?, ?)", (i, self.productColorList[i-1]))
    
    # 상품 DB 생성
    def insertProduct(self):
        for i in range(0, len(self.productNameList)):
            if (self.productTypeList[i] == 1 or self.productTypeList[i] == 4): # 아우터와 잠옷은 색상종류가 없다.
                self.cursor.execute("INSERT INTO products('product_name', 'product_price', 'type_id') VALUES(?, ?, ?)", (self.productNameList[i], self.productPriceList[i], self.productTypeList[i]))
            else:
                for j in range(0, len(self.productColorIdList)):
                    self.cursor.execute("INSERT INTO products('product_name', 'product_price', 'type_id', 'color_id') VALUES(?, ?, ?, ?)", (self.productNameList[i], self.productPriceList[i], self.productTypeList[i], self.productColorIdList[j]))
    
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
            print("상품 타입을 입력해주세요 (아우터 : 1, 상의 : 2, 하의 : 3, 잠옷 : 4) : ")
            searchProductType = int(input())
            if searchProductType < 1 or searchProductType > 4:
                print("상품 타입을 잘못입력하셨습니다.")
                return
            self.cursor.execute("SELECT * FROM products WHERE type_id = ?", (searchProductType,))
            searchProducts = self.cursor.fetchall()
            self.printProducts(searchProducts)

        elif inputValue == "3":
            print("상품 컬러를 입력해주세요 (회색 : 1, 검은색 : 2, 흰색 : 3) : ")
            searchProductColor = int(input())
            if searchProductColor < 1 or searchProductColor > 3:
                print("상품 컬러를 잘못입력하셨습니다.")
                return
            self.cursor.execute("SELECT * FROM products WHERE color_id = ?", (searchProductColor,))
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
        orderProductId = int(input())
        print("수량 : ")
        orderProductNumber = int(input())
        nowDate = datetime.datetime.now().strftime('%Y-%m-%D %H:%M:%S')
        self.cursor.execute("SELECT product_price FROM products WHERE product_id = ?", (orderProductId,))
        orderProductPrice = self.cursor.fetchall()[0][0]
        orderPrice = orderProductNumber * orderProductPrice
        self.cursor.execute("INSERT INTO orders('order_date', 'order_number', 'order_price', 'product_id') VALUES(?, ?, ?, ?)", (nowDate, orderProductNumber, orderPrice, orderProductId))
        print()
        print()

    # 상품 출력
    def printOrders(self, orderList):
        print("{:^20}{:^20}{:^50}{:^20}{:^20}{:^30}".format("order id", "product id", "product name", "price", "number", "order date"))
        for i in orderList:
            ordertId = str(i[0])
            orderDate = str(i[1])
            orderNumber = str(i[2])
            orderPrice = str(i[3])
            productId = str(i[4])
            productName = str(i[5])
            print("{:^20}{:^20}{:^50}{:^20}{:^20}{:^30}".format(ordertId, productId, productName, orderPrice, orderNumber, orderDate))
        print()
        print()

    # 구매 내역 보기
    def showOrder(self):
         print("현재까지의 주문 내역을 확인합니다.")
         self.cursor.execute("SELECT orders.order_id, orders.order_date, orders.order_number, orders.order_price, orders.product_id, products.product_name FROM orders INNER JOIN products ON orders.product_id = products.product_id")
         orderList = self.cursor.fetchall()
         self.printOrders(orderList)

if __name__ == "__main__":
    pass