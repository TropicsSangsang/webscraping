import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("https://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
# browser.find_element(By.ID, "id").send_keys("my_id")
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close()  # 현재창만 닫는다
browser.quit()   # 모든창을 닫는다

while True:
    pass