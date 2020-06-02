height = int(input("Insert the number: "))

for i in range(height):
    # 왼쪽 산
    for j in reversed(range(height)):
        if j > i:
            print(" ", end="")
        else:
            print("*", end="")
    # 오른쪽 산
    for j in range(height):
        if j < i:
            print("*", end="")
    print()
