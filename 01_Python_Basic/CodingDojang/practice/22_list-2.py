## 리스트의 할당과 복사
a = [0, 0, 0, 0, 0]
b = a

print(a is b)
b[2] = 99

print(a)
print(b)

## copy
a = [0, 0, 0, 0, 0]
b = a.copy()

print(a is b)
print(a == b)

b[2] = 99
print(a)
print(b)
