# Section06-3
# Selenium
# Selenium 사용 실습(3) - 실습프로젝트(2)

# 다나와 노트북 Apple 제조사로 크롤링 - 페이지 넘김 추가

# selenium 임포트
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromeDriver.exe', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('./webdriver/chrome/chromeDriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
# browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭1
# Explicitly wait -> 동적. 나타나면 클릭할 수 있다.
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭2
# Implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# Explicityly vs Implicitly 차이점 조사

# 원하는 모델 카테고리 클릭
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label'))).click()

# 2차 페이지 내용
# print(f'After Page Contents : {browser.page_source}')

# 2초간 대기
time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링 페이지 수
target_crawl_num = 5

while cur_page <= target_crawl_num:

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('****** Curtrent Page : {}'.format(cur_page))
    print()

    # 필요 정보 추출
    for v in pro_list:
        # 임시 출력
        # print(v)

        if not v.find('div', class_="ad_header"):
            # 상품명, 이미지, 가격
            print(v.select('p.prod_name > a')[0].text.strip())
            if (v.select('a.thumb_link > img')[0].has_attr('data-original')):
                print(v.select('a.thumb_link > img')[0]['data-original'])
            else:
                print(v.select('a.thumb_link > img')[0]['src'])
            print(v.select('p.price_sect > a > strong')[0].text.strip())

            # 이 부분에서 엑셀 저장(파일, DB 등)
            # CODE
            # CODE

        print()
    print()

    # 페이지 별 스크린 샷 저장
    browser.save_screenshot(f'./website_screenshot/target_page{cur_page}.png')

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawling Succeed.')
        break

    # 페이지 이동 클릭
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'div.number_wrap > a:nth-child({cur_page})'))).click()


    # BeautifulSoup 인스턴스 삭제
    del soup

    # 3초간 대기
    time.sleep(3)

    

# 브라우저 종료
browser.close()