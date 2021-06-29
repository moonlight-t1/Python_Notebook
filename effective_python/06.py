## unpacking
# item = ("apple", "banana")

# first = item[0]
# second = item[1]

# first, second = item
# print(first, "&", second)


favorite_snacks = {"짭조름한 과자": ("프레즐", 100), "달콤한 과자": ("쿠키", 180), "채소": ("당근", 20)}

# unpacking
(
    (type1, (name1, cals1)),
    (type2, (name2, cals2)),
    (type3, (name3, cals3)),
) = favorite_snacks.items()

# dictinary method
print(favorite_snacks.items())
print(favorite_snacks.keys())
print(favorite_snacks.values())

for key, value in favorite_snacks.items():
    print("key:", key, "- value:", value)

# print(f"제일 좋아하는 {type1}는 {name1}, {cals1} 칼로리입니다.")
# print(f"제일 좋아하는 {type2}는 {name2}, {cals2} 칼로리입니다.")
# print(f"제일 좋아하는 {type3}는 {name3}, {cals3} 칼로리입니다.")


## 두 값 바꾸기 - bubble_sort
# def bubble_sort(a):
#     for _ in range(len(a)):
#         for i in range(1, len(a)):
#             if a[i] < a[i - 1]:
#                 a[i - 1], a[i] = a[i], a[i - 1]  # 두 값 바꾸기


# names = ["프레즐", "당근", "쑥갓", "베이컨"]
# bubble_sort(names)
# print(names)

# ### 3개의 값 바꾸기
# a, b, c = 10, 20, 30

# a, b, c = c, b, a
# print(a, b, c)

# ## list unpacking
# snacks = [("베이컨", 350), ("도넛", 240), ("머핀", 190)]

# for rank, (name, calories) in enumerate(snacks, 1):
#     print(f"#{rank}: {name} - {calories}")

