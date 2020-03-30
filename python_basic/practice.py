try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("에러 발생!!!")
    print(e)

print("try-except문을 통과해야만 실행됩니다")