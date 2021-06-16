# 자료형 알아내기
x = 10
y = "str"

print(type(x))
print(type(y))
print()

# 변수 여러 개 한 번에 만들기
x, y, z = 10, 20, 30
print(x, y, z, end=" ")
print("\n")

# 두 변수 교환
x, y = 10, 20
x, y = y, x
print(x, y, end=" ")
print()

# 변수 삭제하기
x = 10
del x
# print(x)  # error

# 빈 변수 만들기
x = None
print(x)

# map을 사용하여 정수로 변환
a, b = map(int, input().split())
print(a + b)

