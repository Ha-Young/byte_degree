# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'http://cafefiles.naver.net/MjAxOTAzMzBfMjA2/MDAxNTUzOTU0NDQ4Njkw.qURce2CpdsPUlUZlvPxEsBxCcTsXh6wgOMSQSrp96tgg.-kIyuDWmkZacQ8TZaryf6ayFyOoNPz3XdNC1QVbX30gg.PNG.5dang99024/Screenshot_2019-03-30-23-00-20.png'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = './test1.jpg'
save_path2 = './index.html'

# 예외 처리
try:
    (file1, header1) = req.urlretrieve(img_url, save_path1)
    (file2, header2) = req.urlretrieve(html_url, save_path2)

except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print(f'Filename1 {file1}')
    print(f'Filename2 {file2}')
    print()

    # 성공
    print('Download Succed')
    