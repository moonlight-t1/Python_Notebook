## 반복 가능한 객체 알아보기
# print(dir([1, 2, 3]))

# print([1, 2, 3].__iter__)

# it = [1, 2, 3].__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# # print(it.__next__()) # StopIteration Exception


## 이터레이터 만들기
# class Counter:
#     def __init__(self, stop):
#         self.current = 0  # 현재 숫자
#         self.stop = stop  # 반복을 끝낼 숫자

#     def __iter__(self):
#         return self  # 현재 인스턴스를 반환

#     def __next__(self):
#         if self.current < self.stop:
#             r = self.current
#             self.current += 1
#             return r
#         else:
#             raise StopIteration


# for i in Counter(3):
#     print(i, end=" ")


# class CountDown:
#     def __init__(self, start):
#         self.start = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start > 0:
#             num = self.start
#             self.start -= 1
#             return num
#         else:
#             raise StopIteration


# for i in CountDown(5):
#     print(i, end=" ")


## __getitem__ 메서드 사용
# class CountDown:
#     def __init__(self, stop):
#         self.stop = stop

#     def __getitem__(self, index):
#         if index < self.stop:
#             return self.stop - index
#         else:
#             raise IndexError


# print(CountDown(3)[0], CountDown(3)[1], CountDown(3)[2])

# for i in CountDown(3):
#     print(i, end=" ")

## iter
# import random

# it = iter(lambda: random.randint(0, 5), 2)  # 2가 나오면 끝난다

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# import random

# for i in iter(lambda: random.randint(0, 5), 2):
#     print(i, end=" ")

# next
it = iter(range(3))

print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))  # 반복이 끝나면 기본값 출력
