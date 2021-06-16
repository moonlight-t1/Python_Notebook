# 심사 문제

age = int(input())
balance = 9000

if age >= 19:
    balance -= 1250
elif 13 <= age < 18:
    balance -= 1050
else:
    balance -= 650

print(balance)

