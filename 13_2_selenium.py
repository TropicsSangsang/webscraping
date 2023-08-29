# selenium 다운 + 크롬 ->도움말 ->크롬 버전(114..) 알고 ->구글에서 chromedriver치고 
# 자기 컴퓨터와 맞는 chromedriver다운-->이걸 본인 프로젝트 옆(안이 아니고)에 압축해제

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium을 사용하여 Chrome 웹 브라우저 열기
browser = webdriver.Chrome() # 현재 드라이버에 있는 chromedriver.exe를 사용하겠다는 의미//"./chromedriver.exe"
browser.get("https://daum.net")

elem = browser.find_element(By.NAME,"q")
elem.send_keys("나도코딩") # 검색창에 나도코딩 쓰기
# elem.send_keys(Keys.ENTER) # 나도코딩 그리고 엔터하기
# browser.back()
# elem.send_keys("나도코딩") # 여기까지 하면 이상하게 창이 꺼져버림. 바로 위까지는 안정적으로 수행
elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]")
# print(elem)
elem.click()
# browser.close()  # 현재창만 닫는다
browser.quit()   # 모든창을 닫는다

while True:
    pass