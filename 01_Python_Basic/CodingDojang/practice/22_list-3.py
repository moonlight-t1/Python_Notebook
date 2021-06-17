## for 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
# for i in a:
#     print(i, end=" ")

## 인덱스를 요소와 함께 출렭하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(a, start=1):
    print(index, value)

for i in range(len(a)):
    print(a[i])

i = 0
while i < len(a):
    print(a[i])
    i += 1

## 리스트의 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
a.sort()
print(a[-1], a[0])


a = [38, 21, 53, 62, 19]
print(max(a), min(a))

## 요소의 합계 구하기
a = [10, 10, 10, 10, 10]
print(sum(a))
