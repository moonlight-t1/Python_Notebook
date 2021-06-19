## 세트에 요소 추가하기
a = {1, 2, 3, 4}
a.add(5)
print(a)

## 세트에서 특정 요소 삭제하기
a.remove(3)  # 요소 없으면 에러 발생
print(a)

a.discard(2)
print(a)
a.discard(3)
print(a)

## 세트에서 임의의 요소 삭제
a = {1, 2, 3, 4}
print(a.pop())
print(a)

## 세트에서 모든 요소 삭제
a.clear()
print(a)
## 세트의 요소 개수 구하기
a = {1, 2, 3, 4}
print(len(a))

## 세트의 할당과 복사
a = {1, 2, 3, 4}
b = a
print(a is b)

b.add(5)
print(a)
print(b)

b = a.copy()
print(a is b)
print(a == b)

b.add(5)
b.add(6)
print(a)
print(b)

## 세트 출력
for i in b:
    print(i)

## 세트 표현식
a = {i for i in "apple"}
print(a)

a = {i for i in "pineapple" if i not in "aple"}
print(a)
