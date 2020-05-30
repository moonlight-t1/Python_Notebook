import requests
import re
from bs4 import BeautifulSoup
import json
import random
import os


# def get_news():
#     url = ""  # 뉴스 url
#     r = requests.get(url)
#     bs = BeautifulSoup(r.text, "lxml")
#     lists = bs.select("")  # 뉴스 기사 목록

#     for li in lists:
#         href = url + li["href"]  # 기사의 url을 원래 url과 이어 붙여준다

#         r = requests.get(href)
#         bs = BeautifulSoup(r.text, "lxml")
#         texts = bs.select("div.[class] > p.[class]")  # p 태그에 있는 각 단락들
#         contents = [p.text for p in texts]  # texts의 리스트화
#         contents = " ".join(contents)  # 리스트를 벗기고 하나의 문자열화
#         return contents.lower()  # 소문자로 변경 후 리턴(테스트로 뉴스 기사 하나만 단어 뽑아낸다)
#     return None

def get_news():
    url = "https://edition.cnn.com/2020/02/10/asia/parasite-south-korea-us-intl-hnk-scli/index.html"  # 뉴스 url
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    texts = bs.select("div.zn-body__read-all > div.zn-body__paragraph")

    contents = [p.text for p in texts]  # texts의 리스트화
    contents = " ".join(contents)  # 리스트를 벗기고 하나의 문자열화

    return contents.lower()  # 소문자로 변경 후 리턴(테스트로 뉴스 기사 하나만 단어 뽑아낸다)


def naver_translate(word):
    try:
        url = "https://ac.dict.naver.com/enkodict/ac?st=11001&q={}".format(
            word)
        r = requests.get(url)
        j = json.loads(r.text)
        return (j["items"][0][0][1][0])
    except:
        return None


def make_quiz(news):

    # 정규식을 이용해서 3 ~ 15개 글자만 추출
    match_pattern = re.findall(r'\b[a-z]{4,15}\b', news)  # 경계 사이의 4~15글자를 뽑아내라

    # 단어가 몇 번 반복하는지 counting
    frequency = {}
    quiz_list = []

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    for word, count in frequency.items():
        if count > 1:
            kor = naver_translate(word)

            if kor is not None:
                quiz_list.append({kor: word})

    return quiz_list


def quiz():
    quiz_list = make_quiz(get_news())
    random.shuffle(quiz_list)

    chance = 5
    count = 0

    for q in quiz_list:
        os.system("cls")
        count += 1
        kor = list(q.keys())[0]
        english = q.get(kor)

        print("=" * 90)
        print("문제 : {}".format(kor))
        print("=" * 90)

        for j in range(chance):
            user_input = str(input("뜻에 맞는 단어 입력하세요 > ")).strip().lower()

            if user_input == english:
                print("정답입니다!! {} 문제 남음".format(len(quiz_list) - count))
                os.system("pause")
                break
            else:
                n = chance - (j + 1)
                if j == 0:
                    print("{}가 아닙니다. {} 번 기회가 남았습니다.".format(user_input, n))
                elif j == 1:
                    print("{}가 아닙니다. {} 번 기회가 남았습니다. 힌트: {}로 시작".format(
                        user_input, n, english[0]))
                elif j == 2:
                    hint = " _ " * int(len(english) - 2)
                    print("{}가 아닙니다. {} 번 기회가 남았습니다. 힌트; {} {} {}로 시작".format(
                        user_input, n, english[0], english[1], hint))
                elif j == 3:
                    hint = " _ " * int(len(english) - 3)
                    print("{}가 아닙니다. {} 번 기회가 남았습니다. 힌트; {} {} {} {}로 시작".format(
                        user_input, n, english[0], english[1], english[2], hint))
                else:
                    print("틀렸습니다.!! 정갑은 {} 입니다.".format(english))
                    os.system("pause")

    print("더 이상 문제가 없습니다")


quiz()
