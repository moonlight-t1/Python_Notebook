stock = {
    "못": 125,
    "나사못": 35,
    "나비너트": 8,
    "와셔": 24,
}

order = ["나사못", "나비너트", "클립"]  # 클립은 없다


## 1
def get_batches(count, size):
    return count // size


result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)  # 8개씩 묶어준다
    if batches:
        result[name] = batches

print(result)

## 2
found = {
    name: get_batches(stock.get(name, 0), 8)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}
print(found)

## 3 warlus
result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}

print(result)

## 4
half = [count // 2 for count in stock.values()]
print(half)
print(count)

## 5 generator
found = (
    (name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8))
)
print(next(found))
print(next(found))

