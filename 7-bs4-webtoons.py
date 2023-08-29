# import requests
# from bs4 import BeautifulSoup

# url ="https://comic.naver.com/webtoon"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# # 네이버 웹툰 전체 목록 가져오기
# cartoons = soup.find_all("span", attrs={"class":"ContentTitle__title--e3qXt"})
# # class 속성이 ContentTitle__title--e3qXt인 모든 "span" element 를 반환
# for cartoon in cartoons:
#     print(cartoons.get_text())   # 모든 만화의 정보를 가져온다고 함

import requests
from bs4 import BeautifulSoup

url = "https://m.dcinside.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# with open("today.html", "w", encoding="utf-8") as f:   # 잘 가져오는지 확인->여기서 잘 안되면 동적 page이므로 selenium으로
#     f.write(soup.prettify())

items = soup.select(".subject-add ")

# print(items)

# print(items[0].text)

# for item in items:
#     print(item)

for e, item in enumerate(items, 1):
    print(f"{e}:{item.text}")


# print(soup.a) 

# print(soup.find("div", attrs={"class":"text_area___K6nq"}))
# cartoons = soup.find("strong", attrs={"class":"title__f6YXl"})


# print(cartoons.get_text()) # //undo

    