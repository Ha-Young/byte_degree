# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명

path_list = ["C:/test1.jpg", "C:/index.html"]

# 다운로드 리소스 url
target_url = ["http://cafefiles.naver.net/MjAxOTEwMjVfMTkx/MDAxNTcxOTc1ODEyNjI5.2wRPvogPzIlHvZqD6Xk6kfbsvuzpv2ksok6QnLHrWHEg.UcCpZ8ZuaeXHqCHKv9dGV11uAUlahR5xYx8S7bUyjAwg.JPEG/7F683D2F-63AD-457B-85F2-9B598578BBDD.jpeg", "http://google.com"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("------------------------------------------------------")

        # 상태 정보 중간 출력
        print(f'Header Info-{i} : {response.info()}')
        print(f'HTTP Status Code: {response.getcode()}')
        print("------------------------------------------------------")


    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ", e.reason)

    #성공
    print()
    print("Download Succeed.")

    with open(path_list[i], 'wb') as c:
        c.write(contents)
