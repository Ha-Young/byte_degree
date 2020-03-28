# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Choi'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
except Exception:
    print('Exception')
else:
    print('Ok! else')
finally:
    print('finally')


print()
print()

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Kim3'
    if a == 'Kim':
        print("허가@")
    else:
        raise ValueError
except ValueError:
    print("문제 발생!")
except Exception as f:
    print(f)
else:
    print("OK!")