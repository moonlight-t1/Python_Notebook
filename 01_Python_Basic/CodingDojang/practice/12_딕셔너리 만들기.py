## 키 이름이 중복되면 (python 3.9)
lux = {"health": 490, "health": 800, "mana": 334, "melee": 550, "armor": 18.72}
print(lux["health"])  # 가장 뒤에 있는 값만 사용

## dict로 딕셔너리 만들기
### 1
lux1 = dict(health=490, mana=332, melee=550, armor=18.72)
print(lux1)

### 2
lux2 = dict(zip(["health", "mana", "melee", "armor"], [490, 334, 550, 18.72]))
print(lux2)

### 3
lux3 = dict([("health", 490), ("mana", 334), ("melee", 550), ("armor", 18.72)])
print(lux3)

### 4
lux4 = dict({"health": 490, "mana": 334, "melee": 550, "armor": 18.72})
print(lux4)

## 딕셔너리의 키에 값 할당하기
lux["health"] = 100
print(lux)

lux["mana_regen"] = 3.18  # 새로운 키와 값 추가
print(lux)

## 딕셔너리에 키가 있는지 확인
print("health" in lux)

print("attack_speed" in lux)

## 딕셔너리의 키 개수 구하기
print(len(lux))

## 딕셔너리 만들기
x = dict()
x = {"a": 10, "b": 20}
x = dict(a=10, b=20)
x = dict({"a": 10, "b": 20})

print(type(x))

## 심사문제
# a = input().split()
# b = map(float, input().split())
# x = dict(zip(a, b))
# print(x)

## 파이썬 3.5 이하에서 딕셔너리의 키의 순서가 보장되도록 만들기
from collections import OrderedDict

lux = OrderedDict(
    {"health": 490, "health": 800, "mana": 334, "melee": 550, "armor": 18.72}
)
print(lux)

