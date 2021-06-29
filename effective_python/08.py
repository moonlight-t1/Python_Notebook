## zip과 딕셔너리

# alpha = ["a", "b", "c"]
# num = [10, 20, 30]

# result = list(zip(alpha, num))
# print(result)
# print(result[0][0])

## dict and zip
# capitals = ["Seoul", "Tokyo", "Paris"]
# countries = ["Korea", "Japan", "France"]
# scores = [10, 20, 30]

# country_dict_1 = dict(zip(capitals, countries))
# print(country_dict_1)

# country_dict_2 = dict(zip(countries, tuple(zip(capitals, scores))))
# print(country_dict_2)


## zip
names = ["Jack", "Tom", "Cecilia"]
counts = [len(n) for n in names]  # 4 3 7

# longest_name = None
# max_count = 0
# # print(list(zip(names, counts)))

# for name, count in zip(names, counts):  # unpacking
#     if count > max_count:
#         longest_name = name
#         max_count = count

# print(longest_name, max_count)

## 서로 길이가 다른 경우
names.append("Rosalind")  # 리스트에 원소 추가
# for name, count in zip(names, counts):
#     print(name)

## zip_longest
import itertools

for name, count in itertools.zip_longest(names, counts, fillvalue=10):
    print(f"{name}: {count}")

