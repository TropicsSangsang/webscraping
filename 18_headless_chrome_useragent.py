from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True    # 크롬창 없이 할려면 이 두줄만 써주면 된다
options.add_argument("window-size=1920x1080") # 이 크기에 맞춰서 브라우져를 띄어서 내부적으로 동작
# 아래 줄이 없으면 headless 사용시 오류가 나올수 있으므로 user-agent 를 이용해서 해결하자
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/114.0.0.0 Safari/537.36

detected_value = browser.find_element(By.ID, "detected_value")
print(detected_value.text)
browser.quit()



