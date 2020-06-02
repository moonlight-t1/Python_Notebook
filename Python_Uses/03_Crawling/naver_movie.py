import requests
from bs4 import BeautifulSoup


def get_movie_point(start, end):

    results = []

    for i in range(start, end + 1):
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'.format(
            i)

        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")

        # 태그 안으로 접근해서 select
        trs = bs.select("table.list_netizen > tbody > tr")

        for tr in trs:
            tds = tr.select("td")
            if len(tds) != 5:
                continue

            number = tds[0].text  # 번호
            point = tds[2].text  # 평점
            movie = tds[3].select("a")[0].text  # 영화제목
            writer = tds[4].select("a")[0].text  # 작성자

            results.append({
                "number": number,
                "movie": movie,
                "writer": writer,
                "point": point
            })

    return results


print(get_movie_point(1, 3))
