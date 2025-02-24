from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 감지 방지
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')  # 일반적인 User-Agent 설정

# 드라이버 초기화
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    # 자동화 감지 관련 속성 제거
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # 구글 웹사이트로 이동
    driver.get("https://www.google.com")
    
    # 랜덤 대기 (2-4초)
    time.sleep(random.uniform(2, 4))
    
    # 검색창 찾기
    search_box = driver.find_element(By.ID, 'APjFqb')
    
    # 검색어를 한 글자씩 자연스럽게 입력
    search_text = '충북과학고등학교'
    for char in search_text:
        search_box.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # 타이핑 간격을 랜덤하게 설정
    
    # 잠시 대기 후 엔터
    time.sleep(random.uniform(0.5, 1.5))
    search_box.send_keys(Keys.ENTER)
     # 검색 결과가 로드될 때까지 잠시 대기
    time.sleep(random.uniform(2, 4))
  

    # CSS 선택자를 사용하여 링크 요소 찾기
    link = driver.find_element(By.CSS_SELECTOR, '#kp-wp-tab-overview > div.TzHB6b.j8lBAb.p7kDMc.cLjAic.K7khPe.LMRCfc > div > div > div > div > div > div > div > div > div > span > a > div > div > div > div.byrV5b > cite')

    time.sleep(random.uniform(1, 2))

    # 링크 클릭
    link.click()

    # 새 페이지가 로드될 때까지 대기
    time.sleep(random.uniform(3, 5))
    
    # 1시간 대기
    time.sleep(3600)

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()