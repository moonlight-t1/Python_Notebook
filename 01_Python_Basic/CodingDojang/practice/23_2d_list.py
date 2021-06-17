## jagged list
a = [[10, 20], [500, 600, 700], [9], [30, 40], [8], [800, 900, 1000]]

print(a)

## pprint
from pprint import pprint

pprint(a, width=20)
# pprint(a, indent=4, width=20)

## for 반복문을 한 번만 사용하기
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)

## 0으로 초기화된 1차원 리스트 만들기
a = [0] * 10
print(a)

## 0으로 초기화된 2차원 리스트 만들기 - 1
a = [[0 for _ in range(4)] for _ in range(4)]  # 4x4
pprint(a, width=20)

## 0으로 초기화된 2차원 리스트 만들기 - 1
a = [[0] * 4 for _ in range(4)]
pprint(a, width=20)

## 톱니형 리스트 만들기
a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(a)

## sorted로 2차원 리스트 정렬하기
students = [["john", "C", 19], ["maria", "A", 25], ["andrew", "B", 7]]

print(sorted(students, key=lambda value: value[0]))
print(sorted(students, key=lambda value: value[1]))
print(sorted(students, key=lambda value: value[2]))


## deep copy
import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

a[0][0] = 100
print(a)
print(b)
