import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)  # url 로 이동

# 가는 날 선택 클릭
# elem = browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6 select_Date__1aF7Y")  # //undo
# elem.click()
# elem = browser.find_element(By.LINK_TEXT, "가는 날") # //undo--> so, XPATH 로 대체함
# elem.click()
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27일, 28일 선택
# browser.find_elements(By.LINK_TEXT, "27")[0].click()   # elements 사용하면 list로 나옴->아래에서는 element사용으로 list가 아님
# browser.find_elements(By.LINK_TEXT, "28")[0].click()  # //undo--> so, XPATH 로 대체함

# 다음달 27일, 28일 선택
# browser.find_elements(By.LINK_TEXT, "27")[1].click()
# browser.find_elements(By.LINK_TEXT, "28")[1].click()  # //undo--> so, XPATH 로 대체함

# 이번달 27일, 다음달 30일 선택 --> 그냥 XPATH 로 해결함
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button/b").click()
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[4]/button/b").click()

# 제주도 선택
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b").click()
# time.sleep(1)
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
# time.sleep(1)
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[2]/span/i[1]").click()
# time.sleep(1)

# 항공권 검색 클릭
# browser.find_element(By.LINK_TEXT, "항공권 검색").click()   # //undo why?
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/button/span").click()  # //do
# browser.find_element(By.CLASS_NAME, "domestic_select_schedule__xWQ-K").click()   # //undo
# time.sleep(10)


# # 첫번째 결과 출력   --> 바로 앞까지 do but 아래 시행하면 클릭과 출력 사이에 로딩 대기 시간때문에 에러가 나옴
# # 이것을 처리하기 위해서 시간 조절이 필요함---> 이거는 다음 편으로..gogo
# elem = browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]/div/button")
# print(elem.text)   # 실행은 된듯 한데 print가 안나오네

while True:
    pass