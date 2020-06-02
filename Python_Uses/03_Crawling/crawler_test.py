"""
1. 원하는 웹페이지에 접속하여 HTML 데이터를 받아온다.
2. 받아온 HTML 데이터를 분석 가능한 형태로 가공한다.
3. 원하는 데이터를 추출한다.
"""

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get("https://www.naver.com")
# print(response.html.links)

response = requests.get("https://www.naver.com")
bs = BeautifulSoup(response.text, "html.parser")  # parser를 통해 text를 분석한다

for img in bs.select("img"):
    print(img)

# print(response.status_code)  # 상태코드 출력
# print(response.headers)  # 헤더값
# print(response.text)  # 디코딩 상태 출력
