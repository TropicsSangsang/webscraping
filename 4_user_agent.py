import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"}
res = requests.get(url, headers=headers)
res.raise_for_status()   # 이렇게 두줄로만 처리하면 된다

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)