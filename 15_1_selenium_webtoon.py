import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3" }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movie = soup.find("img", attrs={"class":"Poster__image--d9XTI"})
print(movie.get_text())

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