keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

# 입력
# alpha bravo charlie delta
# 10 20 30 40

# 키가 'delta'인 키-값 쌍 삭제
del x["delta"]
# 혹은 x.pop('delta')

# 값이 30인 키-값 쌍 삭제
x = {key: value for key, value in x.items() if value != 30}
print(x)
