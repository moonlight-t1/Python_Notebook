## 랜덤
import random

print(random.random())

print(random.randint(1, 6))

## 주사위
i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)

## random.choice
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))

## 심사 문제
money = int(input())

while money - 1350 >= 0:
    money -= 1350
    print(money)

