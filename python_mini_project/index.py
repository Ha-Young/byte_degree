# Byte Degree Python MiniProject 수행
# 2020-02-15 구르딩딩(hychoi)

# -*- coding: utf-8 -*-
import Modules.MiniProject as mpModule
from Modules.myLogger import Log

Log("=====Excute Program=====")
## 데이터베이스를 연결하는 코드 (MiniProject 모듈 클래스 인스턴스 생성)
Log("Connect DataBase...")
miniProject = mpModule.MiniProject()
Log("Connect DataBase Success")

## 상품과 주문 테이블을 생성하는 코드
Log("Create Tables...")
miniProject.createTables()
Log("Create Tables Success")

## 상품 데이터를 추가하는 코드
Log("Insert Datas...")
miniProject.initData()
Log("Insert Datas Success")

input("구르딩딩의 홈쇼핑에 오신것을 환영합니다~ Enter 키를 눌러주세요!")    # Enter Game Start!

# 홈쇼핑 시작
Log("Start Shopping!")
try:
    while True:
        print("원하는 기능의 아래 숫자를 입력해주세요")
        print('1. 상품 검색하여 보기')
        print('2. 전체 상품 보기')
        print('3. 바로 구매하기')
        print('4. 현재까지 구매한 내역 보기')
        print('5. 접속 종료하기')

        inputMenu = input()
        Log("User Input : " + inputMenu)
        print()

        if inputMenu == "1":
            ## 상품 목록을 표시하는 코드
            Log("Search Product...")
            miniProject.searchProduct()
            Log("Search Product Success")
            continue
        elif inputMenu == "2":
            ## 상품 목록을 표시하는 코드
            Log("Show Products...")
            miniProject.showProduct()
            Log("Show Products Success")
            continue
        elif inputMenu == "3":
            Log("Order Product...")
            miniProject.orderProduct()
            Log("Order Product Success")
            continue
        elif inputMenu == "4":
            Log("Show Orders...")
            miniProject.showOrder()
            Log("Show Orders Success")
            continue
        elif inputMenu == "5":
            print("구르딩딩의 홈쇼핑을 이용해주셔서 감사합니다. 다음에 또 방문해주세요~")
            Log("End Shopping!")
            break
        else:
            print("잘못된 명령어를 입력하셨습니다.")
            Log("Wrong Input!")
            continue
except Exception as ex:
    print("예기치 못한 오류로 종료되었습니다. 다시 실행해주세요.\n문제가 반복 될 경우 관리자에게 문의해주세요.")
    Log("error : " + ex)

Log("=====Exit Program=====")