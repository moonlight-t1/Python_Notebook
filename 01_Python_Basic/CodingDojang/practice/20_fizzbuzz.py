## 단축 코드
# for i in range(1, 101):
#     print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)

## 심사 문제
start, stop = map(int, input().split())
for i in range(start, stop + 1):
    print("Fizz" * (i % 5 == 0) + "Buzz" * (i % 7 == 0) or i)
