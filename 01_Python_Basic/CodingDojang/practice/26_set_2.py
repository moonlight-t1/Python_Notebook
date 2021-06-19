## 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))

## 교집합
print(a & b)
print(set.intersection(a, b))

## 차집합
print(a - b)
print(set.difference(a, b))

## 대칭차집합
print(a ^ b)
print(set.symmetric_difference(a, b))

## 집합 연산 후 할당 연산자 사용하기
# update
a = {1, 2, 3, 4}
a |= {5}  # 현재 세트에 다른 세트를 더한다
print(a)

a = {1, 2, 3, 4}
a.update({6})  # 현재 세트에 다른 세트를 더한ㄷ
print(a)

# intersection_update
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4, 5}  # 겹치는 요소만 저장한다.
print(a)

a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4, 5})  # 겹치는 요소만 저장한다
print(a)

# difference_update
a = {1, 2, 3, 4}
a -= {3}  # 현재 세트에서 다른 세트를 뺀다
print(a)
a = {1, 2, 3, 4}
a.difference_update({4})
print(a)

# symmetric_difference_update
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}  # 겹치지 않는 요소만 현재 세트에 저장한다
print(a)

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})  # 겹치지 않는 요소만 현재 세트에 저장한다
print(a)

## 부분 집합과 상위집합 확인하기

# issubset
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})  # 현재 세트가 다른 세트의 부분집힙인지 확인
print(a.issubset({1, 2, 3, 4, 5}))  # 현재 세트가 다른 세트의 부분집합인지 확인

# proper subset
a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5})  # 현재 세트가 다

# issuperset
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})  # 상위집합인지 확인
print(a.issuperset({1, 2, 3, 4}))  # 상위집합인지 확인

# proper superset
a = {1, 2, 3, 4}
print(a > {1, 2, 3})

## 세트가 같은지 다른지 확인
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})
print(a == {4, 2, 1, 3})
print(a != {1, 2, 3})

## 세트가 겹치지 않는지 확인하기
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({3, 4, 5, 6}))
