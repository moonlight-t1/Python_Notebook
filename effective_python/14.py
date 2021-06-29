# ## 1 - sort and sorted
# # sort
# a = [38, 21, 53, 62, 19]
# a.sort()
# print(a)

# # sorted
# a = [10, 20, 30, 15, 20, 40]
# b = sorted(a)  # 정렬된 새 리스트 생성
# print(b)


# # 문자열 정렬
# a = "zbdaf"
# b = sorted(a)
# print(b)

# c = "".join(sorted(a))  # join
# print(c)

## 2차원 리스트 정렬
# students = [["john", "C", 19], ["maria", "A", 25], ["andrew", "B", 7]]

# students.sort(key=lambda value: value[0])
# print(students)
# students.sort(key=lambda value: value[1])
# print(students)
# students.sort(key=lambda value: value[2])
# print(students)

# print(sorted(students, key=lambda value: value[0]))
# print(sorted(students, key=lambda value: value[1]))
# print(sorted(students, key=lambda value: value[2]))

## 2 - 객체 처리
# class Tool:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight

#     def __repr__(self):
#         """
#         In Python format (f-string) strings, what does !r mean? [duplicate]

#         https://stackoverflow.com/questions/44800801/in-python-format-f-string-strings-what-does-r-mean
#         """
#         return f"Tool({self.name!r}, {self.weight})"


# # tools list
# tools = [
#     Tool("수준계", 3.5),
#     Tool("해머", 12.5),
#     Tool("스크류 드라이버", 0.5),
#     Tool("끌", 1.25),
# ]

# print("미정렬: ", repr(tools))
# tools.sort(key=lambda x: x.name)
# print("이름순 정렬: ", tools)
# # tools.sort(key=lambda x: -x.weight)  # 내림차순
# # print("무게순 정렬: ", tools)

## 3 - weight로 먼저 정렬 후 name으로 정렬
# print(dir(tuple))  # lesser than

# drill = (4, "드릴")
# sander = (4, "연마기")
# assert drill[0] == sander[0]
# assert drill[1] < sander[1]
# assert drill < sander

# power_tools = [
#     Tool("드릴", 4),
#     Tool("원형 톱", 5),
#     Tool("착암기", 40),
#     Tool("연마기", 4),
# ]

# print(power_tools)
# power_tools.sort(key=lambda x: (-x.weight, x.name), reverse=True)
# print(power_tools)

# ## sort 여러번 호출 & stable 정렬
# power_tools.sort(key=lambda x: x.name)  # name 오름차순
# power_tools.sort(key=lambda x: x.weight, reverse=True)  # weight 기준 내림차순
# print(power_tools)

## 정렬하기 전에 key 함수를 사용해 원소 값 변형
# places = ["home", "work", "New York", "Paris"]
# places.sort()
# print("대소문자 구분: ", places)
# places.sort(key=lambda x: x.lower())
# print("대소문자 무시: ", places)

