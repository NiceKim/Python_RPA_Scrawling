## test
#import requests
#from bs4 import BeautifulSoup

#url = "https://m.blog.naver.com/PostList.naver?blogId=organistgabriel&categoryName=%EC%84%B1%EA%B0%80%282015%29%ED%95%B8%EB%93%9C%EB%B6%81&categoryNo=16"
#res = requests.get(url)
#res.raise_for_status()

# CASE1 : write resquest -> HTML File, No Content
#with open("extra/test1.html", "w", encoding="utf8") as f:
#    f.write(res.text)

#soup = BeautifulSoup(res, "lxml")

# CASE2 : write soup.text -> Text only
# with open("extra/test2.html", "w", encoding="utf8") as f:
#    f.write(soup.text)

# CASE3 : write soup.prettify -> HTML File, pretty, No content
# with open("extra/test3.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())

# CASE4 : Get with Useragent -> HTML File, pretty, still No content
# with open("extra/test4.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())


# CASE5 : Webdriver Scroll -> HTML File, Pretty, with all contents
############## ############### ############### ############### ############### ############### ############### ###############
# 스크롤링

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)
url = "https://m.blog.naver.com/PostList.naver?blogId=organistgabriel&categoryName=%EC%84%B1%EA%B0%80%282015%29%ED%95%B8%EB%93%9C%EB%B6%81&categoryNo=16"
browser.get(url)
#browser.maximize_window()

gap = 1
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    time.sleep(gap)
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == prev_height:
        break
    prev_height = current_height
    
print("Scroll Done")
##########################################################################################################################################################################
### BS 작업

import requests
from bs4 import BeautifulSoup

## bs4 + selenium 사용 : 스크롤링에 시간이 소요, 파일로 저장해서 시간 단축 
soup = BeautifulSoup(browser.page_source, "lxml")

with open("source.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
    
browser.close()