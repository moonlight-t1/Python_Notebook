import requests
from bs4 import BeautifulSoup
import json
import time

KAKAO_TOKEN = "djPb1fT8uDhjGJACmir_jqCG00kbi8YATDQFdgopb9UAAAFwNGNjmQ"


# 카카오톡 메세지
def send_kakao(text):
    header = {"Authorization": "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}

    r = requests.post(url, headers=header, data=data)
    print(r.text)


# 핫딜 정보 가져오기
def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&pp=20".format(
        keyword)

    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []

    for r in rows:
        link = r.select("a.dealTitle")[0]
        href = link.get("href")  # href가 없으면 None이 저장된다
        if href is None:
            continue
        href = "https://slickdeals.net" + href
        title = link.text

        price = r.select("span.price")[0].text.replace(
            "$", "").replace("from", "").strip()

        if price.find("/") >= 0 or price == "":  # 요금제나 가격이 없는 경우 continue
            continue
        price = float(price)
        hot = len(r.select("span.icon-fire"))  # 핫딜
        results.append((title, href, price, hot))
    return results


send_lists = []


def main():
    keyword = "ipad"
    max_price = 300.0

    while True:
        results = get_hotdeal(keyword)
        if results is not None:
            for r in results:
                title, href, price, hot = r  # unpacking
                if price < max_price:
                    if title not in send_lists:
                        msg = "{} {} {} {}".format(title, price, hot, href)
                        send_kakao(msg)
                        send_lists.append(title)
        time.sleep(60 * 5)


main()
