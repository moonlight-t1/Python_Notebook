keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {key: value for key, value in x.items() if value != 30}
x = {key: value for key, value in x.items() if key != "delta"}

print(x)
