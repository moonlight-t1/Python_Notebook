import random

words_dict = {
    "사자": "lion",
    "호랑이": "tiger",
    "사과": "apple",
    "비행기": "airplane"
}

# 딕셔너리에는 순서의 개념이 없다
# 그래서 키들만 따로 젖아하는 배열을 만들어준다.
words = []

# 키 값만 배열에 담고 섞어준다(shuffle)
for word in words_dict:
    words.append(word)

random.shuffle(words)

chance = 3
for i in range(0, len(words)):
    q = words[i]
    for j in range(0, chance):
        user_input = str(input("{}의 영어 단어를 입력하세요 > ".format(q)))
        answer = words_dict[q]  # 키를

        # 공백제거, 소문자
        if user_input.strip().lower() == answer.lower():
            print("정답 입니다.")
            break
        else:
            print("틀렸습니다")

    if user_input != answer:
        print("정답은 {} 입니다.".format(answer))

print("모든 문제를 다 풀었습니다.")
