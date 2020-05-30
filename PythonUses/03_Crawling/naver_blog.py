import requests
from bs4 import BeautifulSoup


def get_search_naver_blog(query, start_page=1, end_page=None):
    start = (start_page - 1) * 10 + 1  # 51 = (6 - 1) * 10 + 1
    url = "https://search.naver.com/search.naver?where=post&query={}&start={}".format(
        query, start)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    result = []

    if end_page is None:
        # 1-10 / 18,655건
        tot_counts = bs.select("li.sh_blog_top")[0].text
        # 18,655건
        tot_counts = tot_counts.split("/")[-1]
        # 18655
        tot_counts = int(tot_counts.replce("건", "").replace(",", "").strip())

        # end_page 계산
        end_page = int(tot_counts / 10)
        if tot_counts % 10 > 0:
            end_page += 1

        # 페이지 제한
        if end_page > 900:
            end_page = 900

    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try:
            thumbnail = li.select("img")[0]["src"]  # 썸네일 이미지 경로
            title = li.select("dl > dt > a")[0]  # 타이틀
            summary = li.select("dl > dd.sh_blog_passage")[0].text  # 요약

            title_link = title["href"]  # 타이틀 링크
            title_text = title.text  # 타이틀 제목

            result.append((thumbnail, title_text, title_link, summary))

        except:
            continue

    # 시작 페이지가 끝 페이지보다 작으면 함수 재귀호출
    if start_page < end_page:
        start_page += 1
        result.extend(get_search_naver_blog(
            query, start_page=start_page, end_page=end_page))

    return result


results = get_search_naver_blog("박은빈", start_page=1, end_page=3)

for result in results:
    print(result)
