# import requests
# from bs4 import BeautifulSoup


# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# links = soup.find_all("li", attrs={"class":"item__O332w"})
# print(len(links))

# for link in links:
#     print(link.text)

# # with open("test1.html", "w", encoding="utf8") as f:
# #    f.write(res.text)

# # with open("test2.html", "w", encoding="utf8") as f:
# #    f.write(soup.text)

# # with open("test3.html", "w", encoding="utf8") as f:
# #    f.write(soup.prettify())

# with open("test4.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())

############### ############### ############### ############### ############### ############### ############### ###############
## 스크롤링

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# browser = webdriver.Chrome(options=chrome_options)


# url = "https://m.blog.naver.com/PostList.naver?blogId=organistgabriel&categoryName=%EC%84%B1%EA%B0%80%282015%29%ED%95%B8%EB%93%9C%EB%B6%81&categoryNo=16"
# browser.get(url)
# #browser.maximize_window()

# import time
# gap = 1

# prev_height = browser.execute_script("return document.body.scrollHeight")

# while True:
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
#     time.sleep(gap)
#     current_height = browser.execute_script("return document.body.scrollHeight")
#     if current_height == prev_height:
#         break

#     prev_height = current_height

# print("Scroll Done")

#########################################################################################################################################################################
## BS 작업

import requests
from bs4 import BeautifulSoup

## bs4 + requests만 사용 : 대기/스크롤링 없어서 자료 없음
# res = requests.get(url, headers=headers) 
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

## bs4 + selenium 사용 : 스크롤링에 시간이 소요, 파일로 저장해서 시간 단축 
# soup = BeautifulSoup(browser.page_source, "lxml")

# with open("test5.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())

# HTML 파일 사용
with open("test5.html", "rt", encoding="utf8") as f:
    soup = BeautifulSoup(f, "html.parser")



########################################################
lists = soup.find_all("div", attrs={"class":"text_area___UrFH"})
print(len(lists))

i = 0
for list in lists:
    title = list.find("strong", attrs={"class":"title__tl7L1 ell2"}).get_text()
    title = title.lstrip()
    if not str.isdigit(title[0]):
        continue
    link = list.find("a").attrs['href']
    print(title)
    print(link)
    i+=1
    if i > 10:
        break

