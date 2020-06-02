import requests
from bs4 import BeautifulSoup
import pandas


def get_movie_point(start, end=1):
    results = []

    for i in range(start, end+1):
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'.format(
            i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")
        trs = bs.select("table.list_netizen > tbody > tr")
        for tr in trs:  # 다수의 평점
            # 번호
            number = tr.select_one("td.ac.num").text
            # 작성자
            writer = tr.select_one("td.num > a.author").text

            # td 의 title 클래스를 구합니다.
            tr_data = tr.select_one("td.title")

            # td class="title" 자식중 최초 a 태그안에 제목만 추출
            title = tr_data.select_one("a").text

            # td class="title" 자식중 div 태그 자식중 em 태그에 점수 추출
            point = tr_data.select_one("div.list_netizen_score > em").text

            # td class="title" 태그에서 a, div, br 태그 제거
            # extract() 함수는 태그와 태그의 내용까지 모두 제거합니다.
            [x.extract() for x in tr_data.select("a")]
            [x.extract() for x in tr_data.select("div")]
            [x.extract() for x in tr_data.select("br")]

            # 위에서 태그를 모두 제거한 tr_data에서 내용만 추출
            content = tr_data.text.strip()

            results.append([title, point, writer])

    return results


column = ["영화제목", "점수", "작성자"]
results = get_movie_point(1, 3)

dataframe = pandas.DataFrame(results, columns=column)  # 판다스의 데이터 형태로 저장
print(dataframe)

# 엑셀로 저장
dataframe.to_excel("movie.xlsx", sheet_name="네이버평점", header=True, startrow=1)
