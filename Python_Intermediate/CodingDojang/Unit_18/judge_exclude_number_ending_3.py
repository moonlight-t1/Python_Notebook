start, stop = map(int, input("Insert two numbers: ").split())

i = start

for i in range(start, stop + 1):
    if i % 10 == 3:
        continue
    else:
        print(i, end=" ")

