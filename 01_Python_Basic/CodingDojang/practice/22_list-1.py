## append
a = [10, 20, 30]
a.append(500)  # 원소 추가
print(a)
print(len(a))


a = [10, 20, 30]
a.append([500, 600])  # 리스트 안에 리스트 추가
print(a)
print(len(a))

## extend
a = [10, 20, 30]
a.extend([500, 600])  # 리스트 확장하기
print(a)
print(len(a))

## insert
a = [10, 20, 30]
a.insert(2, 500)  # 리스트의 특정 인덱스에 요소 추가
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(len(a), 500)  # 끝에 추가
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(1, [500, 600])  # 리스트 안에 리스트 추가
print(a)
print(len(a))

a = [10, 20, 30]
a[1:1] = [500, 600]  # 리스트 중간에 여러 요소 추가
print(a)
print(len(a))

## pop
a = [10, 20, 30, 40]
a.pop()  # 맨 끝의 요소 빼내기
print(a)
print(len(a))

a = [10, 20, 30, 40]
a.pop(1)  # 인덱스 1을 빼내게
print(a)
print(len(a))

a = [10, 20, 30, 40]
del a[1]  # 인덱스 1요소 삭제하기
print(a)
print(len(a))

## remove
a = [10, 20, 30, 20]  # 리스트에 값이 여러개 있는 경우
a.remove(20)  # 처음 찾은 값 삭제
print(a)
print(len(a))

## deque
from collections import deque

a = deque([10, 20, 30])
print(a)
a.append(500)
a.popleft()
print(a)

## 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))

## 특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))

## 리스트의 순서 뒤집기
a = [10, 20, 30, 40, 50, 60]
a.reverse()
print(a)

## 리스트의 요소 정렬하기
a = [10, 20, 30, 15, 20, 40]
a.sort()  # 사용한 리스트 변경
print(a)

a = [10, 20, 30, 15, 20, 40]
b = sorted(a)  # 정렬된 새 리스트 생성
print(b)

## 리스트의 모든 요소 삭제
a = [10, 20, 30]
a.clear()  # clear
print(a)

a = [10, 20, 30]
del a[:]
print(a)

## 리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a) :] = [500, 600]  # 리스트 끝에 값 추가
a.extend([700, 800])  # extend
print(a)

## 리스트가 비어있는지 확인
seq = []
if seq:
    print(seq[-1])
else:
    print("It is empty")

## 리스트의 특정 원소 개수 세기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))
