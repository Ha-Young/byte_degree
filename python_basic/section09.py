# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(content))
# 반드시 close 리소스 반환
f.close()

print("-----------------------------")

# 예제2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("-----------------------------")

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())   # strip -> 줄바꿈, 끝 공백 제거
print("-----------------------------")

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()     # 커서가 끝에 있기 때문에 더이상 읽을 내용이 없다.
    print(">", content)    # 내용 없음

print("-----------------------------")

# 예제5 (한줄 씩 읽기)
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='###')
        line = f.readline()

print("-----------------------------")
print("-----------------------------")

# 예제6 (전체 다 읽기 -> 리스트로 (한줄씩 담겨있음))
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end= ' ****** ')

print("-----------------------------")
print("-----------------------------")

# 예제7 
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

# ===========================================================
# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('NiceMan!')

# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('GoodMan!')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5 (print함수 이용)
with open('./resource/text3.txt', 'w') as f:
    print('Test Contents1!', file=f)
    print('Test Contents1!', file=f)

