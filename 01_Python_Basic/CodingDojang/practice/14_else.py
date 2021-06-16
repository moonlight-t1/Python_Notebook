## 조건부 표현식(conditional expression)
x = 5
y = x if x == 10 else 0
print(y)

## 부등호 연달아 사용
if 0 < x < 20:
    print("x is lesser than 20")

## 심사문제
a, b, c, d = map(int, input().split())
if (0 <= a <= 100) and (0 <= b <= 100) and (0 <= c <= 100) and (0 <= d <= 100):
    if (a + b + c + d) / 4 >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 입력")
