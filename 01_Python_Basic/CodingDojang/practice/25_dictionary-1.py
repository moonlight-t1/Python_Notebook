## setdefault: 이미 존재하는 것은 setdefault로 수정 불가
x = {"a": 10, "b": 20, "c": 30, "d": 40}
x.setdefault("e")  # 새 원소 추가(Noned으로 초기화)
print(x)
x.setdefault("f", 100)
print(x)

## 딕셔너리의 값 수정하기
x.update(a=100)
print(x)
x.update(e=500)  # 없는 키면 새로 추가

y = {1: "one", 2: "two"}
y.update({1: "ONE", 2: "TWO", 3: "THREE"})  # 딕셔너리 넣어 수정
print(y)

y.update([[2, "TWO"], [4, "FOUR"]])  # 리스트로 업데이트
print(y)

y.update(zip([5, 6], ["FIVE", "SIX"]))  # zip과 리스트로 업데이트
print(y)

## 딕셔너리에서 키-값 쌍 삭제하기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.pop("a"))
print(x.pop("z", 100))  # 키 값이 없을 때는 기본값만 반환한다

del x["b"]  # del로 삭제하기
print(x)

## popitem()
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.popitem())  # 마지막 값 삭제하고 key-value 튜플 형태로 리턴

## 딕셔너리의 모든 키-값 쌍을 삭제하기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
x.clear()
print(x)

## 딕셔너리에서 키의 값을 가져오기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.get("b"))

## 딕셔너리에서 키-값 쌍을 모두 가져오기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.items())  # items()는 키-값 쌍을 모두 가져온다

for key, value in x.items():
    print(key, "=", value)

print(x.keys())  # keys()는 키를 모두 가져온다
for key in x.keys():
    print(key, end=" ")

print()
print(x.values())  # values()는 값을 모두 가져온다
for value in x.values():
    print(value, end=" ")

print()
## 리스트와 튜플로 딕셔너리 만들기
keys = ["a", "b", "c", "d"]
values = [10, 20, 30, 40, 50]

x = dict.fromkeys(keys)  # 값을 모두 None으로 초기화
print(x)

y = dict.fromkeys(keys, 100)  # 값을 모두 100으로 초기화
print(x)

z = dict(zip(keys, values))  # zip을 이용해 key, value 지정
print(z)

## defaultdict
from collections import defaultdict

y = defaultdict(int)

y["z"]  # 기본값 0으로 초기화
print(y)

z = defaultdict(lambda: 100)  # 기본값 100으로 초기화
z["a"]
print(z)

## Counter
from collections import Counter

print(Counter("hello world"))
print(Counter("hello world").most_common())
print(Counter("hello world").most_common(1))

## 딕셔너리 표현식
keys = ["a", "b", "c", "d"]
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

y = {key: 0 for key in dict.fromkeys(["a", "b", "c", "d"]).keys()}  # 키만 가져온다
print(y)

z = {value: 0 for value in {"a": 10, "b": 20, "c": 30, "d": 40}.values()}  # 값을 키로 사용
print(z)

u = {
    value: key for key, value in {"a": 10, "b": 20, "c": 30, "d": 40}.items()
}  # 키-값 자리를 바꿈
print(u)

## 딕셔너리 표현식에서 if 조건문 사용하기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
x = {
    key: value for key, value in x.items() if value != 20
}  # 삭제할 키-값 쌍을 제외하고 남은 키-값 쌍으로 딕셔너리 새로 만든다
print(x)

## 딕셔너리 안에 딕셔너리 사용하기
terrestrial_planet = {
    "Mercury": {"mean_radius": 2439.7, "mass": 3.3022e23, "orbital_period": 87.969},
    "Venus": {"mean_radius": 6051.8, "mass": 4.8676e24, "orbital_period": 224.70069,},
    "Earth": {"mean_radius": 6371.0, "mass": 5.97219e24, "orbital_period": 365.25641,},
    "Mars": {"mean_radius": 3389.5, "mass": 6.4185e23, "orbital_period": 686.9600,},
}

print(terrestrial_planet["Venus"]["mean_radius"])  # 6051.8

## 딕셔너리 복사
import copy
from pprint import pprint

x = {"a": 0, "b": 0, "c": 0, "d": 0}
y = x.copy()
print(y)

z = copy.deepcopy(terrestrial_planet)  # 중첩 딕셔너리 복사
pprint(z, width=20)


terrestrial_planet = {
    "Mercury": {"mean_radius": 2439.7, "mass": 3.3022e23, "orbital_period": 87.969},
    "Venus": {"mean_radius": 6051.8, "mass": 4.8676e24, "orbital_period": 224.70069,},
    "Earth": {"mean_radius": 6371.0, "mass": 5.97219e24, "orbital_period": 365.25641,},
    "Mars": {"mean_radius": 3389.5, "mass": 6.4185e23, "orbital_period": 686.9600,},
}

# 이렇게 하면 key 값이 출력된다
for i in terrestrial_planet:
    print(i)
