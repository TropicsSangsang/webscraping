# selenium 다운 + 크롬 ->도움말 ->크롬 버전(114..) 알고 ->구글에서 chromedriver치고 
# 자기 컴퓨터와 맞는 chromedriver다운-->이걸 본인 프로젝트 옆(안이 아니고)에 압축해제

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium을 사용하여 Chrome 웹 브라우저 열기
browser = webdriver.Chrome() # 현재 드라이버에 있는 chromedriver.exe를 사용하겠다는 의미//"./chromedriver.exe"
browser.get("https://naver.com")



elem = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW') 
# elem = browser.find_element_by_class_name("MyView-module__link_login___HpHMW")  # 현재 이거는 안됨

print(elem)   # 이렇게 하면 엘리먼트 객체를 가져옴
elem.click()   # 아이디 클릭 까지 나옴
browser.back()  # 브라우저 뒤로
browser.forward()  # 브라우저 앞으로
browser.refresh()  # 새로고침
browser.back()
elem = browser.find_element(By.ID,"query") # 검색창 찾기
print(elem)
elem.send_keys("나도코딩") # 검색창에 나도코딩 쓰기
elem.send_keys(Keys.ENTER)  # Keys.ENTER를 위해 from selenium.webdriver.common.keys import Keys 필요//나도코딩 그리고 엔터하기

# elem = browser.find_element(By.TAG_NAME,"a")
elem = browser.find_elements(By.TAG_NAME,"a")   # find_elements
# print(elem)

for e in elem:
    print(e.get_attribute("href"))

browser.get("http://daum.net")
elem = browser.find_element(By.NAME,"q")
elem.send_keys("나도코딩") # 검색창에 나도코딩 쓰기
elem.send_keys(Keys.ENTER) # 나도코딩 그리고 엔터하기

while True:
    pass