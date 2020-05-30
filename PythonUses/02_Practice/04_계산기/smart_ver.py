# 5 + 5 * 10 = 100 순차적으로 계산이 되게 만들어야 한다
import os
os.system("cls")

operator = ["+", "-", "*", "/", "="]  # 연산자 목록


def string_calculator(user_input, show_history=False):
    string_list = []
    lop = 0  # 연산자 위치

    # 맨 마지막 위치에 = 연산자를 넣어 이전 값을 취할 수 있게 만든다
    if user_input[-1] not in operator:
        user_input += "="

    # 연산자의 위치를 찾아
    # 연산자가 있는 경우 앞의 값을 취한다
    for i, s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i + 1

    string_list = string_list[:-1]  # 삽입했던 마지막의 = 연산자를 빼준다

    # 계산식을 입력하세요 > 10 + 20 * 3
    # ['10 ', '+', ' 20 ', '*', ' 3']
    # ['10 ', '+', ' 20 ', '*', ' 3']
    # ['30', '*', ' 3']
    # ['90']

    pos = 0  # 현재 위치
    while True:
        if pos + 1 > len(string_list):
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            # 연산자를 기준으로 앞 뒤 숫자를 계산해준다
            # 그리고 이를 temp에 넣는다
            temp = string_list[pos - 1] + \
                string_list[pos] + string_list[pos + 1]
            del string_list[0:3]  # 앞에서부터 3개 지워준다
            string_list.insert(0, str(eval(temp)))  # temp 계산 결과를 맨 앞으로 끼워 넣는다
            pos = 0  # pos 위치를 원래대로 0의 위치로 보낸다

            # 계산과정을 보여준다
            if show_history:
                print(string_list)

        pos += 1

    if len(string_list) > 0:
        result = float(string_list[0])

    return round(result, 4)


while True:
    os.system("cls")
    user_input = input("계산식을 입력하세요 > ")
    if user_input == "q":
        break
    result = string_calculator(user_input, show_history=True)
    print("결과: {}".format(result))
    os.system("pause")
