import requests

# res = requests.get("http://naver.com")
# res = requests.get("http://nadocoding.tistory.com")
# print("응답코드 :", res.status_code)   # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code,"]")


# res.raise_for_status()
# print("웹 스크래핑을 진행합니다")


res = requests.get("http://google.com")
res.raise_for_status()   # 이렇게 두줄로만 처리하면 된다

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)