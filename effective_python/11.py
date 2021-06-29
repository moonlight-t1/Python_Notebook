# str = "hello"

# str_copy = str[::-1]  # reverse
# print(str_copy)

# str_copy = str[::]
# print(str_copy)

## Shallow Copy
a = [10, 20, 30]

b = a
a[0] = 100
print(b)

## Deep Copy - 1
a = [10, 20, 30, 40, 50]
b = a[:]
a[0] = 100
print(a)
print(b)

## Deep Copy - 2
a = [10, 20, 30, 40, 50]
b = a.copy()
a[0] = 100
print(a)
print(b)

## Deep Copy - 3
import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

a[0][0] = 100
print(a)
print(b)
