# install beautifulsoup4   스크래핑을 위한 패키지
# install lxml   구문분석을 위한 parser
import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 우리가 가져온 html문서를(res.text) lxml이라는 파써를 통해서...
# ...BeautifulSoup 객체를 만들었음...그 모든 정보를 soup이 가지고 있는 상태임

with open("today1.html", "w", encoding="utf-8") as f:   # 잘 가져오는지 확인->여기서 잘 안되면 동적 page이므로 selenium으로
    f.write(soup.prettify())


# print(soup.title)  # <title>Google 뉴스</title>
# print(soup.title.get_text())   # Google 뉴스
# print(soup.a)  # print(soup.a) 코드는 BeautifulSoup 객체인 soup에서 첫 번째 <a> 태그를 출력하는 것입니다.  //동적page로 undo
                    # ...실행하면 soup 객체에서 첫 번째로 발견되는 <a> 태그의 내용이 출력됩니다.
                    # 만약 <a> 태그가 없다면 None이 출력될 것입니다.
# print(soup.a.attrs) # a element의 속성 정보를 출력  //undo
# print(soup.a["href"]) # a element의 속성 '값' 정보를 출력 //undo

# print(soup.find("a"))  //undo
# print(soup.find("a", attrs={"class":"WwrzSb"})) # 뒤의 정보("a", attrs={"class":"WwrzSb"})에서 처음으로 발견되는(find) element 출력
# print(soup.find(attrs={"class":"WwrzSb"}))  # 하나만 있는 경우는 이렇게 속성으로만으로도 가능
# print(soup.find("strong", attrs={"class":"auto-titles size-16 line-4x2 auto-fontA onload"}))
# print(soup.find("li", attrs={"class":"AsideList__item--i30ly"}))
# rank1 = soup.find("li", attrs={"class":"AsideList__item--i30ly"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
