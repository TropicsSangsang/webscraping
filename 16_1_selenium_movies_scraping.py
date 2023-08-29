
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?hl=ko&gl=US"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")  # 1920 x 1080

# 화면 가장 아래로 스크롤 내리기
# document.body.scrollHeight : 문서의 바디 총 높이(사이트의 총 높이가 아님)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스트롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스트롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")



import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class":"VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  MPNOXb"})
# print(len(movies))
# movies = soup.find_all("div", attrs={"class":["hP61id", "Epkrse"]}) # ->클래스를 두개 중 아무거나 받아야 하는 경우(or 개념) 라스트로 감싸서...

movies = soup.find_all("div", attrs={"class":"hP61id"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)    

    #  할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "  <할인되지 않은 영화 제외>")
        continue     

    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()   

    # 링크 정보
    # link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"] # 링크만 안됨
    # link = movie.find("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"}).find("a")["href"]  # //undo
    # 올바른 링크 : https://play.google.com +link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    # print("링크 : ","https://play.google.com" + link) # 링크만 안됨
    
    print("-" * 120)


browser.quit()








while True:
    pass
