# Byte Degree Python MiniProject 수행
# 2020-02-15 구르딩딩(hychoi)

# -*- coding: utf-8 -*-
import MiniProject as mpModule

## 데이터베이스를 연결하는 코드 (MiniProject 모듈 클래스 인스턴스 생성)
miniProject = mpModule.MiniProject()

## 상품과 주문 테이블을 생성하는 코드
miniProject.createTables()

## 상품 데이터를 추가하는 코드 
miniProject.initData()

input("구르딩딩의 홈쇼핑에 오신것을 환영합니다~ Enter 키를 눌러주세요!")    # Enter Game Start!

# 홈쇼핑 시작
try:
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
            ## 상품 목록을 표시하는 코드
            miniProject.searchProduct()
            continue
        elif inputMenu == "2":
            ## 상품 목록을 표시하는 코드
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
except Exception as ex:
    print("예기치 못한 오류로 종료되었습니다. 다시 실행해주세요.\n문제가 반복 될 경우 관리자에게 문의해주세요.")