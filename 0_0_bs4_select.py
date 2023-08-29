import requests
from bs4 import BeautifulSoup

url = "https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.select(".news_tit")

print(items)

# print(items[0].text)

# for item in items:
#     print(item)

for e, item in enumerate(items, 1):
    print(f"{e}:{item.text}")


# print(soup.a) 

# print(soup.find("div", attrs={"class":"text_area___K6nq"}))
# cartoons = soup.find("strong", attrs={"class":"title__f6YXl"})


# print(cartoons.get_text()) # //undo
