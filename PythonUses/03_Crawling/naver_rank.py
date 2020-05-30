import requests
from bs4 import BeautifulSoup
import time


# 함수 동작 시간 측정
def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper


@time_function
def r_find_all(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li", {"class": "ah_item"})

    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles


@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)

    lists = bs.select("li.ah_item")

    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles


url = "https://www.naver.com"
r_find_all(url, "html.parser")
r_select(url, "html.parser")

r_find_all(url, "lxml")
r_select(url, "lxml")


# r = requests.get("https://www.naver.com")
# bs = BeautifulSoup(r.text, "lxml")

# lists = bs.select("li.ah_item")
# for li in lists:
#     title = li.select("span.ah_k")[0].text
#     print(title)

# lists = bs.find_all("li", {"class": "ah_item"})  # 클래스 이름으로 li를 찾는다

# for li in lists:
#     # 클래스 이름으로 span을 찾는다
#     # 태그 사이의 내용만 가져온다
#     title = li.find("span", {"class": "ah_k"}).text
#     print(title)
