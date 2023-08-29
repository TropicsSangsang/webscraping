import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8", newline="") #  newline을 공백으로 하면 한칸 띄우는것이 사라진다
writer = csv.writer(f)       # 만약 엑셀에서 한글이 꺠지면 utf-8 -> utf-8-sig 로 바꿔준다

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# 현재 탭으로 구분되어 있는 string을 split("\t")가 -->["N", "종목명", "현재가",...]로 만들어준다
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res =requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)  # writerow 안에는 리스트로 받아줘야...
        # 실행하면 왼쪽에 csv파일이 생겨남.


