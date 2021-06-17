## list comprehension
a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(10)]
print(c)

d = [i * 2 for i in range(10)]
print(d)

## 리스트 표현식에서 if 조건문 사용하기
a = [i for i in range(10) if i % 2 == 0]
print(a)

## 이중 리스트 만들기
a = [[0 for _ in range(4)] for _ in range(4)]
print(a)

## for 반복문과 if 조건문 여러 번 사용하기
a = [i * j for j in range(2, 10) for i in range(1, 10)]  # 뒤에서부터 앞으로
print(a)

## input
a = input().split()
print(a)  # 리스트

## map
a = map(int, input().split())  # map으로 str->int
print(list(a))

