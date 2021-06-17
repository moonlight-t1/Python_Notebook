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

