from collections import namedtuple

# namedtuple
Classes = namedtuple("Classes", ["rank", "number"])

# group list
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

# create 80 students
students = [Classes(rank, number) for rank in ranks for number in numbers]

# print(len(students))
# print(students)

# method 2 (recommended)
students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]

# print(students2)

for s in students:
    print(s)