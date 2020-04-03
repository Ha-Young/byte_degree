# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <h1>this is h1 area2</h1>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">lacie</a>
            <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""

# 예제1(BeautifulSoup 기초)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))
print('prettify', soup.prettify())

# h1 태그 접근 (제일 먼저 찾은거 가져온다)
h1 = soup.html.body.h1
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p
print('p1', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling # b태그 갔다가 다음 p
print('p2', p2) 

print('p1 next', p1.next_sibling) # 한번호출하면 태그 끝에간다.

print('p1 next * 3', p1.next_sibling.next_sibling.next_sibling)

print('p1 next * 4', p1.next_sibling.next_sibling.next_sibling.next_sibling)

# 텍스트 출력1
print('h1 >>', h1.string)

# 텍스트 출력2
print('p1 >>', p1.string) # b 태그 무시

# 함수 확인
print(dir(p2))

print()

# 다음 엘리먼트 확인
print(p2.next_element)

# 반복 출력 확인
for v in p2.next_element:
    print(v)

print()
print()

# 예제2(Find, Find_all)
# bs4 초기화

soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
link1 = soup.find_all('a') # limit = 2 옵션
# print(type(link1))
# 리스트 요소 확인
print('links', link1)

print()

# 중요 #
# 태그 자식, 스트링값등으로 조회 가능
link2 = soup.find_all("a", class_='sister') # id="link2", string="title", string=["Elsie", "Title"]
print(link2)

for t in link2:
    print(t)

print()

# 처음 발견한 a 태그 선택
link3 = soup.find("a")
print(link3)
print(link3.string)
print(link3.text)

print()

# 다중 조건
link4 = soup.find("a", {"class": "sister", "data-io": "link3"})
print(link4)
print(link4.string)
print(link4.text)

print()

# css 선택자 : select, select_one
# 태그로 접근 : find, find_all

# 예제3(select, select_one)
# 태그 + 클래스 + 자식선택자
link5 = soup.select_one('p.title > b')
print(link5)
print(link5.string)
print(link5.text)

print()

link6 = soup.select_one("a#link1")
print(link6)
print(link6.string)
print(link6.text)

print()

link7 = soup.select_one("a[data-io='link3']")
print(link7)
print(link7.string)
print(link7.text) 

print()

#. : 클래스, # : id

# 선택자에 맞는 전체 선택
link8 = soup.select('p.story > a')
print(link8)
# print(link8.string)
# print(link8.text) 

print()

link9 = soup.select('p.story > a:nth-of-type(2)')
print(link9)

print()

link10 = soup.select("p.story")
print(link10)

print()

for t in link10:
    temp = t.find_all("a")
    
    if temp:
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else:
        print('-----', t.string)

print()