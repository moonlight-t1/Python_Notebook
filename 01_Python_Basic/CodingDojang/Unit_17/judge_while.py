balance = int(input())
fee = 1350

while 1:
    balance -= fee
    if balance < 0:
        break
    print(balance)
