# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies?hl=ko&gl=US"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3" }

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# # movies = soup.find_all("div", attrs={"class":"VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  MPNOXb"})
# # print(len(movies))
# movies = soup.find_all("div", attrs={"class":"hP61id"})
# print(len(movies))

# # with open("movie.html", "w", encoding="utf-8") as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify())
    
# for movie in movies:
#     title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
#     print(title)    



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

while True:
    pass
