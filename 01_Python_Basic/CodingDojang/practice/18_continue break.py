## 심사 문제
start, stop = map(int, input().split())

i = start

while True:
    if i > stop:
        break
    if (0 <= i < 100) and (i % 10 == 3):
        i += 1
        continue
    if (100 <= i <= 200) and (i % 100 == 3):
        i += 1
        continue
    print(i, end=" ")
    i += 1
