## 튜플에서 특정 값의 인덱스 구하기
a = tuple(range(10, 60, 10))
print(a.index(20))

## 특정 값 개수 구하기
a = (10, 20, 30, 15, 20, 30)
print(a.count(20))

## 튜플 표현식
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

## tuple에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

## 최대, 최소, 합
print(min(a))
print(max(a))
print(sum(a))
