import requests
from bs4 import BeautifulSoup


for year in range(2018, 2023):
    
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    

    for idx, image in enumerate(images, 1):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https" + image_url

        print(image_url)       
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx), "wb") as f: # 영화포스터는 글자가 아닌 데이터이므로 binary의미인 w에 b까지 붙어야...
            f.write(image_res.content)  # image_res가 가지고 있는 content(이것이 이미지)정보를 쓰는 것...

        if idx >= 5:
            break