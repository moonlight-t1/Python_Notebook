import os
import requests
from bs4 import BeautifulSoup


# 파일 목록 구하는 함수
def get_dir_list(dir):
    str_list = ""
    if os.path.exists(dir):
        file_list = os.listdir(dir)
        file_list.sort()
        for f in file_list:
            full_path = os.path.join(dir, f)
            if os.path.isdir(full_path):
                f = "[" + f + "]"  # [폴더명] 형식으로 출력
            str_list += f
            str_list += "\n"
    str_list.strip()
    return str_list


# 날씨 구하기
def get_weather(where):
    weather = ""
    # div.today_area > div.main_info
    url = "https://search.naver.com/search.naver?query={}+날씨".format(
        where)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    w_box = bs.select("div.today_area > div.main_info")

    if len(w_box) > 0:
        temperature = bs.select("span.todaytemp")
        cast_text = bs.select("p.cast_txt")
        indicator = bs.select("span.indicator")

        # 자료들이 존재한다면 출력
        if len(temperature) > 0 and len(cast_text) > 0 and len(indicator) > 0:
            temperature = temperature[0].text.strip()
            indicator = indicator[0].text.strip()
            txt = cast_text[0].text.strip()

            # print(temperature, indicator, txt)

            # 텔레그램에서 엔터 \r\n
            weather = "{}℃\r\n{}\r\n{}".format(temperature, indicator, txt)
    return weather


MONEY_NAME = {
    "유로": "유럽연합 EUR",
    "엔": "일본 JPY (100엔)",
    "위안": "중국 CNY",
    "홍콩달라": "홍콩 HKD",
    "대만달라": "대만 TWD",
    "파운드": "영국 GBP",
    "달라": "미국 USD",
}


# 환율 정보
def get_exchange_info():
    EXCHANGE_LIST = {}
    url = "https://finance.naver.com/marketindex/exchangeList.nhn"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    trs = bs.select("table.tbl_exchange > tbody > tr")
    for tr in trs:
        tds = tr.select("td")
        name = tds[0].text.strip()
        value = tds[1].text.strip().replace(",", "")
        EXCHANGE_LIST[name] = value
    return EXCHANGE_LIST


def money_translate(keyword):
    EXCHANGE_LIST = get_exchange_info()
    keywords = []
    for m in MONEY_NAME.keys():
        if m in keyword:
            # '150 달라' 이렇게 띄어진 것을 붙여준다.
            keywords.append(keyword[0:keyword.find(m)].strip())
            keywords.append(m)
            break

    if keywords[1] in MONEY_NAME:
        country = MONEY_NAME[keywords[1]]

        if country in EXCHANGE_LIST:
            money = float(EXCHANGE_LIST[country])
            if country == "일본 JPY (100엔)":
                money /= 100

            money = format(round(float(money) * float(keywords[0]), 3), ",")
            output = "{} 원".format(money)
            return output


if __name__ == "__main__":
    print(money_translate("50        달라"))
