import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3" }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명//모두 이름이 있으므로 if 필요X
    price = item.find("strong", attrs={"class":"price-value"}).get_text()   # 가격
    rate = item.find("em", attrs={"class":"rating"})   # 평점//평점이 없는 상품때문에 if문 필요
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음" 
   
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점 없음"

    print(name, price, rate, rate_cnt)
        

    
