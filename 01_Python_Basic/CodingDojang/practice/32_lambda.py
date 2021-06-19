## 람다 표현식으로 함수 만들기
plus_ten = lambda x: x + 10

print(plus_ten(10))

y = 20
print((lambda x: x + y)(1))

## 람다 표현식을 인수로 사용하기
a = list(map(plus_ten, [1, 2, 3]))
print(a)

## map 사용하기
a = list(range(1, 11))
b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))

print(b)

c = list(map(lambda x: x + 10 if x % 2 == 0 else x, a))
print(c)

### map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
c = list(map(lambda x, y: x * y, a, b))
print(c)

## filter 사용하기
def f(x):
    return x > 5 and x < 10


a = [8, 3, 2, 10, 1, 5, 7, 1, 9, 0, 11]
print(list(filter(f, a)))


print(list(filter(lambda x: x > 5 and x < 10, a)))

## reduce
def f(x, y):
    return x + y


a = [1, 2, 3, 4, 5]
from functools import reduce

print(reduce(f, a))

print(reduce(lambda x, y: x + y, a))
