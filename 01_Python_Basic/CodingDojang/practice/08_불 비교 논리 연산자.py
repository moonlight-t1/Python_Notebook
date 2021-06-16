# 객체가 같은지 다른지 비교
print(1 == 1.0)  # 값 자체를 비교
print(1 is 1.0)  # 객체를 비교
print(1 is not 1.0)  # 객체를 비교
## 값의 비교에는 is를 사용하면 안된다.
"""
a = -5
print(a is -5)
a = -6
print(a is -6)  # 메모리 주소가 달라질 수도 있다.
"""

# id 확인
a = 100000
b = 100000
print(id(a))
print(id(b))
print(id(100000))

# 심사 문제
a, b, c, d = map(int, input().split())
print(a >= 90 and b > 80 and c > 85 and d >= 80)
