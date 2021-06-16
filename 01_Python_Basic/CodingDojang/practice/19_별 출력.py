## 대각선으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

##
# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print("*", end="")
#     print()

## 산 모양으로 별 찍기
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
