# 타이핑 게임

import time
import random
import os

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

    if user_input == "/exit":
        break

    correct = 0  # 맞은 갯수
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1

    total_len = len(q)
    c = correct / total_len * 100  # 정확도
    e = (total_len - correct) / total_len * 100  # 오타율
    speed = (correct / end_time) * 60  # 분당 속도

    print("속도 : {:0.2f}, 정확도 : {:0.2f}, 오타율 : {:0.2f}".format(speed, c, e))
    os.system("pause")
