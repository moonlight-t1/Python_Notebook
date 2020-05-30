age = int(input())
balance = 9000

if age > 19:
    balance -= 1250
elif age >= 13 and age <= 18:
    balance -= 1050
else:
    balance -= 650

print(balance)
