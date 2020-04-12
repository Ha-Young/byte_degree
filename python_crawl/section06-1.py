# Section06-1
# Selenium
# Selenium 사용 실습(1) - 설정 및 기본 테스트
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# Selenium 공식문서
# https://selenium-python.readthedocs.io/getting-started.html

# 참고자료 - 필독
# https://www.popit.kr/web-scraping-by-selenium/

# 다음 검색 후 해당 페이지 스크린샷

# selenium 임포트
from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 속성 확인
print(dir(browser))

# 브라우저 사이즈
# browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()
# browser.maximize_window()

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용
# print(f'Page Contents : {browser.page_source}')

print()

# 세션 값 출력
# print(f'Session ID : {browser.session_id}')

# 타이틀 출력
# print(f'Title : {browser.title}')

# 현재 URL 출력
# print(f'URL : {browser.current_url}')

# 현재 쿠키 정보 출력
# print(f'Cookies : {browser.get_cookies()}')

# 검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('하트시그널3')

# 검색 (Form Submit)
element.submit()

# 스크린 샷 저장1
browser.save_screenshot("./website_screenshot/screenshot1.png")

# 스크린 샷 저장2
browser.get_screenshot_as_file("./website_screenshot/screenshot2.png")

# 브라우저 종료
browser.quit()

