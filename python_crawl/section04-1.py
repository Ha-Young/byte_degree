# section04-1
# Requests
# requests 사용 스크랩핑(1) - Session

import requests
import urllib.request
# 세션 활성화
# s = requests.Session()


# # 세션 비활성화
# s.close()

# 세션 활성화 - with -> 자동해제
# with requests.Session() as s:
#     r = s.get('https://www.naver.com')

    # 수신 데이터
    # print(r.text)

    # 수신 상태 코드
    # print('Status Code : {}'.format(r.status_code))

    # 확인 -> 코드보다 많이 사용
    # print('OK? : {}'.format(r.ok))
    
# 쿠키 Return
# 테스트에 좋은 사이트 : https://httpbin.org
# jsonplaceholder -> 이 싸이트도 테스트하기 괜찮다. (section04-2)

with requests.Session() as s:
    r = s.get('https://httpbin.org/cookies', cookies={'name':'Kim1'})

    print(r.text)

    # 쿠키 Set
    r2 = s.get('https://httpbin.org/cookies/set', cookies={'name':'Kim2'})
    
    print(r2.text)

    # User-Agent
    url = 'https://httpbin.org'
    headers = {'user-agent': 'nice-man_1.0.0_win10_ram16_home_chrome'}

    # Header 정보 전송
    r3 = s.get(url, headers=headers, cookies={'name':'Kim3'})
    print(r3.text)

