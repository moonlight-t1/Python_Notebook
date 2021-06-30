## unpacking

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]

car_ages_descending = sorted(car_ages, reverse=True)

oldest, second_oldest, *others = car_ages_descending

print(oldest, second_oldest, others)

## empty list
short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)

## iterator unpacking
def generate_csv():
    yield ("날짜", "제조사", "모델", "연식", "가격")


# all_csv_rows = list(generate_csv())
# header = all_csv_rows[0]
# rows = all_csv_rows[1:]


it = generate_csv()
header, *rows = it
print("CSV 헤더: ", header)
print("행 수: ", len(rows))

