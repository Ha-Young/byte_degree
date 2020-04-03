# section03-3

# 다음 주식 정보 분석
# Fake-UserAgent 사용 - pip install fake-useragent
# Header 정보 삽입
# 수신 데이터 가공 및 추출

# URL 요청 했을 때 원했던 데이터가 없으면
# Chrome 브라우저 개발탭의 Network에서 찾아봐야 한다.
# 비동기로 가져오는 데이터이기 때문.
# 해당 API를 사용해야 한다.

# 하지만 해당 API로 직접 접근하면 권한오류로 403코드가 뜬다.
# 그래서 해더 정보를 세팅해줘야 한다.

# user-agent
# refer 등등

import json
import urllib.request as req
from fake_useragent import UserAgent

# Fake Header정보(가상으로 User-agent 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random) <- random도 가능

# 헤더 정보
headers = {
    'User-agent': ua.random,
    'referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# 응답 데이터 확인(Json Data)
print(res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']

# 중간 확인
# print('중간 확인 : ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm))
    print(f'순위 : {elm["rank"]}, 금액 : {elm["tradePrice"]}, 회사명 : {elm.get("name")}')
    
    # 파일(csv, 엑셀, TXT) 저장 및 db 저장
    
