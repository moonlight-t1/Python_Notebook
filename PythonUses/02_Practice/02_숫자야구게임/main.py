import random
import os

numbers = []  # 숫자를 담을 배열
number = str(random.randint(0, 9))  # 숫자는 문자로 저장한다

# 랜덤 숫자 3개를 중복되지 않게 배열에 담는다
for i in range(3):
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number)

os.system("cls")

print("="*60)
print("야구게임을 시작합니다!!!")
print("="*60)

count_strike = 0
count_ball = 0

while count_strike < 3:
    count_strike = 0
    count_ball = 0
    # 인덱싱을 하기 위해 사용자에게 입력받은 숫자를 문자로 변환한다.
    num = str(input("숫자 3자리를 입력하세요> "))
    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:  # 자리도 같고, 위치도 같다면 스트라이크
                    count_strike += 1
                elif num[i] == numbers[j] and i != j:  # 값만 같고, 자리가 다르면 볼
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("3 아웃!!")
        else:
            output = ""
            if count_strike > 0:
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0:
                output += " {} 볼".format(count_ball)
            print(output.strip())

print("게임 성공")
