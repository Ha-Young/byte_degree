# Section 02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print("\"Hello\" \"Python!\"")

print()

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes',)

print()

# format 사용 []대괄호 {}중괄호 ()소괄호
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0} {2}".format('You', 'Me', "Love"))
print("{a} are {b}".format(a="gaga", b="me"))

print()

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ("Hayoung", 7)) 

print("Test1: %5d, Price: %7.2f" % (776, 534.123))
print("Test1: {0: 5d}, Price: {1: 7.2f}".format(776, 534.123))
print("Test1: {a: 5d}, Price: {b: 8.2f}".format(a=776, b=534.123))

#   \n : 개행
#   \t : 탭
#   \\ : 문자
#   \' : 문자
#   \" : 문자
#   \r : 캐리지 리턴
#   \f : 폴 피드
#   \a : 벨 소리
#   \b : 백 스페이스
#   \000 : 널 문자
#   '''
#   """

print('')