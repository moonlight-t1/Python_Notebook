# Chapter04-02
# 파이썬 심화
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))  # 목과 나머지 반환
print(divmod(*(100, 9)))  # 튜플을 언패킹 해서 삽입
print(*(divmod(100, 9)))  # 결과값을 푼다

print()

x, y, *rest = range(10)  # x, y 외 나머지 값들은 리스트에 패킹
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(id(l))
print(id(m))

l *= 2
m *= 2

print(id(l))
print(id(m))

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func..

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango',
          'papaya', 'lemon', 'strawberry', 'coconut']

print('sorted -', sorted(f_list))  # 기본 오름차순
print('sorted -', sorted(f_list, reverse=True))  # 역순 출력
print('sorted -', sorted(f_list, key=len))  # 문자의 길이 순으로 정렬
# key에 함수 직접 입력 가능 끝 글자 기준
print('sorted -', sorted(f_list, key=lambda x: x[-1]))
# 위 결과 반대로
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()

print('sorted -', f_list)  # 원본 출력

print()

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)
