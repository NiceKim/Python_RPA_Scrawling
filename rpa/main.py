# 날짜 : 2023년 06월 11일
# 프로젝트 : 성공회 성가 가사 수집 프로젝트
# 학습목표 : 파이썬, 웹 크롤링, RPA

# 경고메세지 끄기
import warnings
warnings.filterwarnings(action='ignore')
# 다시 출력하게 하기
#warnings.filterwarnings(action='default')

# HTML 파일에서 링크 수집
from lyrics_crawling import *
links, titles = ft_get_links("extra/test5.html")

# 링크 들어가서 가사 수집
lyrics = ft_get_lyrics(links)

# csv 파일로 출력
index = 0
for link in links:
	print(titles[index])
	print(lyrics[index])
	index += 1

