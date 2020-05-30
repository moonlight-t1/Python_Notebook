'''
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032

초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28
'''
import time
import os
import random
CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
       "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
        "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ",
        "ㄾ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]


def break_korean(string):
    word_list = list(string)
    break_word = []

    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            # 유니코드상 몇번째 글자인지 인덱스를 구한다
            char_index = ord(k) - ord('가')

            # 초성 = (유니코드인덱스 / 28) / 21
            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1])

            # 중성 = (인덱스 / 28) % 21
            char2 = int((char_index / 28) % 21)
            break_word.append(JUNG[char2])

            # 종성 = 인덱스 % 28
            char3 = int(char_index % 28)

            if char3 > 0:
                break_word.append(JONG[char3])

        else:
            break_word.append(k)

    return break_word


WORD_LIST = [
    "죽는 날까지 하늘을 우러러",
    "한점 부끄럼이 없기를",
    "잎새에 이는 바람에도",
    "나는 괴로워했다.",
    "별을 노래하는 마음으로",
    "모든 죽어가는 것을 사랑해야지",
    "그리고 나한테 주어진 길을",
    "걸어가야겠다.",
    "오늘 밤에도 별이 바람에 스치운다."
]

random.shuffle(WORD_LIST)  # 리스트를 섞어준다

for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()  # 시작시간
    user_input = str(input(q + '\n')).strip()  # 공백을 벗겨준다
    end_time = time.time() - start_time  # 종료시간

    # 문제와 사용자 입력을 쪼개준다
    src = break_korean(q)
    tar = break_korean(user_input)

    if user_input == "/exit":
        break

    correct = 0  # 맞은 갯수
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1

    total_len = len(src)
    c = correct / total_len * 100  # 정확도
    e = (total_len - correct) / total_len * 100  # 오타율
    speed = (correct / end_time) * 60  # 분당 속도

    print("속도 : {:0.2f}, 정확도 : {:0.2f}, 오타율 : {:0.2f}".format(speed, c, e))
    os.system("pause")

user_input = input("입력> ")
word_list = list(user_input)
