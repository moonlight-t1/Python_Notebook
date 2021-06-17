str = "51900;83000;158000;367500;250000;59200;128500;1304000"

numbers = list(map(int, str.split(";")))
numbers.sort(reverse=True)

for num in numbers:
    num = format(num, ",")
    print(num.rjust(9))
