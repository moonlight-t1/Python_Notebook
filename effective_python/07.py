## lazy generator
flavor_list = ["바닐라", "초콜릿", "피칸", "딸기"]

it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list):
    print(f"{i + 1}: {flavor}")

