import requests
from bs4 import BeautifulSoup

url = "https://www.dcinside.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.select(".box.besttxt")

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
