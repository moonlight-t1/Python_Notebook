num1, num2 = map(int, input().split())
num1 = {i for i in range(1, num1 + 1) if num1 % i == 0}
num2 = {i for i in range(1, num2 + 1) if num2 % i == 0}

divisor = num1 & num2
print(divisor)

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
