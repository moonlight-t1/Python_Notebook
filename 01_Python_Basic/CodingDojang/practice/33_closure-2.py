def countdown(n):
    tmp = n  # 인자로 받은 숫자 저장

    def down():
        nonlocal tmp  # 지역변수 tmp를 수정하기 위한 nonlocal
        n = tmp
        tmp -= 1
        return n

    return down


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=" ")
