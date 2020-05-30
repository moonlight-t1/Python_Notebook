a, b, c, d = map(int, input().split())
average = float((a + b + c + d) / 4)

if a > 100 or b > 100 or c > 100 or d > 100:
    print("Wrong input")
else:
    print(average)

    if average >= 80:
        print("Pass")
    else:
        print("Failed")
