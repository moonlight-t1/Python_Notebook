# sep로 값 사이에 문자 넣기
print(1, 2, 3, sep=", ")

# 개행
print("a", "b", "c", sep="\n")

# 사용하기
print(1, 2, 3, end=" ")

print("hello", "python", end="\n")
print("hello", "python", sep="\n")

# 심사문제 1
# year, month, day, hour, minute, second = input().split()
# print(year, month, day, sep="-", end="T")
# print(hour, minute, second, sep=":")

# getrefcount
import sys

print(sys.getrefcount(1000))  # 현재 객체가 몇 번 사용되었는지 확인

x = 1000
print(sys.getrefcount(1000))

y = 1000
print(sys.getrefcount(1000))

print(x is y)
