import requests
from bs4 import BeautifulSoup
import re


def search_google(keyword, start_page, end_page=None):
    url = "https://www.google.com/search?&q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet".format(
        keyword)

    # user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div > div.rc > div.r > a")

    results = []

    # 끝 페이지 찾기
    if end_page is None:
        counts = bs.select("div#resultStats")[0].text.replace(
            "검색결과 약", "").replace("개", "").replace(",", "").split("(")[0].strip()
        end_page = int(int(counts) / 10)
        if end_page > 10:
            end_page = 10

    for a in links:
        href = a["href"]
        text = a.select("h3")
        if len(text) <= 0:
            continue

        title = text[0].text

        try:
            r = requests.get(href)  # 각 사이트 접속
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(
                r'magnet:\?xt=*'))  # 정규표현식으로 마그넷을 찾는다

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                results.append({
                    "magnet": magnet,
                    "title": title
                })
        except:
            pass

    if start_page < end_page:
        start_page += 10
        results.extend(search_google(keyword, start_page, end_page=end_page))

    return results


results = search_google("기생충", 0)

for r in results:
    print(r)
