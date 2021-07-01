numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}  # 우선 정렬 목록


## closure
def sort_prioriy(numbers, group):
    found = False

    def helper(x):
        nonlocal found  # nonlocal
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


s = sort_prioriy(numbers, group)
print(dir(s))


# sort_prioriy(numbers, group)
# print(numbers)

## class
# class Sorter:
#     def __init__(self, group):
#         self.group = group
#         self.found = False

#     def __call__(self, x):
#         if x in self.group:
#             self.found = True
#             return (0, x)
#         return (1, x)


# sorter = Sorter(group)
# numbers.sort(key=sorter)
# assert sorter.found is True
# print(numbers)


## closure
# def calc():
#     a = 3
#     b = 5

#     def mul_add(x):  # 인자를 받으면 여기로 들어간다
#         return a * x + b  # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산

#     return mul_add  # 함수 자체를 반환(이름만 반환해야 한다


# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))
