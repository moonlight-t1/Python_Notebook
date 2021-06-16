# 짝수 리스트
a = list(range(0, 12, 2))
print(a)

# 튜플 만들기
a = (10,)
print(a)

a = 10, 20, 30, False, "Hello"  # 이것도 튜플
print(a)

# range로 튜플 만들기
a = tuple(range(0, 12, 2))
print(a)

# 리스트와 튜플 안에 문자열 넣기
str = "hello"
print(list(str))
print(tuple(str))

# 리스트 언패킹, 튜플 언패킹
x = [1, 2, 3]
a, b, c = x
print(a, b, c)

x = (1, 2, 3)
a, b, c = x
print(a, b, c)

# 심사 문제
n = int(input())
t = tuple(range(-10, 10, n))
print(t)
