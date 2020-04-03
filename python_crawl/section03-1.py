# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러 정보
print(f'type : {type(mem)}')
print(f'geturl : {mem.geturl()}')
print(f'status : {mem.status}')
print(f'headers : {mem.getheaders()}')
print(f'getcode : {mem.getcode()}')
print(f'read : {mem.read(100).decode("utf-8")}')
print(f'parse : {urlparse("http://www.encar.co.kr?test=test")}')
print(f'parse : {urlparse("http://www.encar.co.kr?test=test").query}')


print()
print("=====================")
print()

# 기본 요청2 (ipify)
API = "https://api.ipify.org"

# Get 방식 Parameter
values = {
    'format': 'json' # text, jsonp
}

print(f'before param : {values}')
params = urllib.parse.urlencode(values)
print(f'after param : {params}')

# 요청 URL 생성
URL = API + "?" + params
print(f"요청 URL = {URL}")

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

print(f'response Data : {data}')

# 수신 데이터 디코딩
text = data.decode('UTF-8')
print(f'response Encoded Data: {text}')

