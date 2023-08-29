# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net 접속
# 2. "송파 헬리오시티" 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# =========== 매물 1 ===========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# =========== 매물 2 ===========
# ...

# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

import requests 
from bs4 import BeautifulSoup

url = "https://realty.daum.net/home/apt/danjis/38487?map=apt"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"}
res = requests.get(url, headers=headers)
res.raise_for_status()   # 이렇게 두줄로만 처리하면 된다
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf-8") as f:   # 잘 가져오는지 확인->여기서 잘 안되면 동적 page이므로 selenium으로
#     f.write(soup.prettify())

data_rows = soup.find_all("div", attrs={"class":"css-1dbjc4n"})
# for row in data_rows:
#     name = row.find("div", attrs={"class":"css-1563yu1"}).get_text()  # 매매유형
#     # area = row.find("div", attrs={"class":"css-1563yu1"})            # 면적
#     # price = row.find("strong", attrs={"class":"price-value"}).get_text()   # 가격
#     # floor = row.find("em", attrs={"class":"css-1563yu1"})            # 층 


data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")


# name = data_rows.find("div", attrs={"class":"css-1563yu1"}).get_text()
# print(name)

# print(name, area, price, floor)


    # print("========== 매물 {} ===========".format(index))
    # print("거래 :", column[0].get_text())
    # print("면적 :", column[1].get_text(),"(공급/전용)")
    # print("가격 :", column[2].get_text(),"(만원)")
    # print("동 :", column[3].get_text())
    # print("층 :", column[4].get_text())






    

        



