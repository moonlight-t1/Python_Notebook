# 특정 값이 있는지 확인하기
print("P" in "Hello, Python")

a = range(0, 100, 10)
print(100 not in a)

# 시퀀스 객체 연결하기
a = [1, 2, 3]
b = [10, 20, 30]
c = a + b
print(c)

# 문자열에 숫자 연결
str = "Hello " + str(10)
print(str)

# 시퀀스 객체 반복하기
a = [1, 2, 3] * 3
print(a)
b = "hello" * 3
print(b)

# 리스트와 튜플 요소 개수 구하기
a = [1, 2, 3]
print(len(a))

b = (1, 2, 3, 4)
print(len(b))

c = "hello"
print(len(c))

print(len(range(0, 10, 2)))

# UTF-8 문자열의 바이트 수 구하기
hello = "안녕하세요"
print(len(hello.encode("utf-8")))  # UTF-8에서 한글 글자 하나는 3바이트

# 인덱스로 접근
r = range(0, 10, 2)
print(r[2])

# __getitem__ 메서드
a = [38, 21, 53, 62, 19]
print(a.__getitem__(1))

# 음수 인덱스 지정하기
print(a[-1])
print(a[-5])

# 마지막 요소에 접근
print(a[-1])
print(a[len(a) - 1])

# del로 시퀀스 객체의 요소 삭제
"""
range, tuple, str은 삭제 불가
"""
a = [1, 2, 3, 4, 5]
del a[2]
print(a)

# 슬라이스 사용하기
a = list(range(0, 100, 10))
print(a[2:8:3])

# 인덱스 생략하기
print(a[:7])
print(a[7:])
print(a[:])
print(a[:7:2])
print(a[7::2])
print(a[::2])
print(a[::])

# 슬라이스 인덱스 음수로 지정
print(a[5:1:-1])
print(a[::-1])

# len 응용하기
print(a[0 : len(a)])
print(a[: len(a)])

# slice 객체 사용하기
print(range(10)[slice(4, 7, 2)])
print(range(10).__getitem__(slice(4, 7, 2)))

# slice에 요소 할당하기
a = list(range(0, 100, 10))
a[2:5] = ["a", "b", "c"]
print(a)

a = list(range(0, 100, 10))
a[2:5] = ["a"]
print(a)

a = list(range(0, 100, 10))
a[2:5] = ["a", "b", "c", "d", "e"]
print(a)

a = list(range(0, 100, 10))
a[2:8:2] = ["a", "b", "c"]
print(a)

# del로 슬라이스 삭제하기
a = list(range(0, 100, 10))
del a[2:5]
print(a)

a = list(range(0, 100, 10))
del a[2:8:2]
print(a)

## 심사 문제 1
# x = input().split()
# y = tuple(x[0 : len(x) - 5])
# print(y)

## 심사 문제 2
s1 = input()
s2 = input()
print(s1[1::2] + s2[0::2])
