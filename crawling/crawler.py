# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 동적으로 데이터를 수집하는 방법
# 매크로처럼 네이버검색시 로그인부터 검색까지 가능

#웹 스크래핑 (Scrapping) : 웹 페이지의 응답을 받아 데이터를 분석하여 필요한 데이터를 수집하는 방법

#파이썬 스크래핑 패키지 : beautifulsoup4 
#파이썬 크롤링 패키지 : selenium

#pip install beautifulsoup4
#pip install selenium 
#pip install beautifulsoup4 selenium

#requests를 하기위한 설치
#pip install requests



#  요청을 하면 반드시 response 로옴 / 존재하는 웹페이지의 경우
# RESPONSE 100 추가 요청 기다림
# RESPONSE 200 요청 성공
# RESPONSE 300 리소스 위치 바뀜
# RESPONSE 400 요청자(클라이언트) 잘못 입력됨
# RESPONSE 500 응답자(서버) 오류
# http response code : 구글에 검색시 오류에대한 정확한 내용을 볼 수 있음

import requests  
from bs4 import BeautifulSoup

URL = 'https://naver.com'

response = requests.get(URL)  

print(response)
print(response.status_code)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.perser')
    print(soup)
else:
    print(response.status_code)


