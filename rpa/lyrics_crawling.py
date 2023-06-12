


def ft_get_links(file_name):
    # CASE 1: bs4 + requests -> No Contents
    #res = requests.get(url) 
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, "lxml")

    # CASE 2: bs4 + selenium -> Has Contents, Takes time to scroll 
    #soup = BeautifulSoup(browser.page_source, "lxml")

    #with open("test5.html", "w", encoding="utf8") as f:
    #    f.write(soup.prettify())

    # CASE 3: HTML 파일 읽기 ->  Has Contents, Save Time 
    import requests
    from bs4 import BeautifulSoup
    
    with open(file_name, "rt", encoding="utf8") as f:
        soup = BeautifulSoup(f, "html.parser")

    lists = soup.find_all("div", attrs={"class":"text_area___UrFH"}) 
    titles = []
    links = []
    for list in lists:
        title = list.find("strong", attrs={"class":"title__tl7L1 ell2"}).get_text()
        title = title.lstrip().rstrip()
        if not str.isdigit(title[0]):
            continue
        link = list.find("a").attrs['href']
        titles.append(title)
        links.append(link)
    print(f'{len(links)}개 링크 수집')
    return (links, titles)
    
def ft_get_lyrics(links):
    lyrics = ["작업 중"]
    return lyrics