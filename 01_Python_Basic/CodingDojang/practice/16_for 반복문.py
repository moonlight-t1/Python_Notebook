## 뒤집어서 출력
for i in reversed(range(10)):
    print(i, end=" ")
print()

for letter in reversed("Python"):
    print(letter, end=".")
print()

for i in reversed(range(10, 21)):
    print(i, end=" ")
print()

## 심사 문제
n = int(input())
for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")

