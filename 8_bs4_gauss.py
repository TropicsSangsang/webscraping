import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# with open("today2.html", "w", encoding="utf-8") as f:   # 잘 가져오는지 확인->여기서 잘 안되면 동적 page이므로 selenium으로
#     f.write(soup.prettify())

items = soup.select(".api_txt_lines.total_tit")

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
