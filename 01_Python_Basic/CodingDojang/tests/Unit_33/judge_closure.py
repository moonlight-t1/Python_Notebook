def countdown(n):
    i = n

    def count():
        nonlocal i
        r = i
        i -= 1
        return r

    return count


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=" ")
