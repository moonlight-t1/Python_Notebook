## 제너레이터 만들기


# def number_generator():
#     yield 0
#     yield 1
#     yield 2


# # for i in number_generator():
# #     print(i)

# # ## 제너레이터 객체가 이터레이터인지 확인
# g = number_generator()
# print(g)
# print(dir(g))

## yield의 동작 과정 알아보기
# def number_generator():
#     yield 0  # 0을 함수 바깥으로 전달하면서 코드 실행을 바깥에 양보
#     yield 1  # 1을 함수 바깥으로 전달하면서 코드 실행을 바깥에 양보
#     yield 2  # 2을 함수 바깥으로 전달하면서 코드 실행을 바깥에 양보


# g = number_generator()

# a = next(g)  # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나온다
# print(a)

# b = next(g)
# print(b)

# c = next(g)
# print(c)

## 제너레이터 만들기
# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1


# for i in number_generator(3):
#     print(i, end=" ")

## yield에서 함수 호출하기
# def upper_generator(x):
#     for i in x:
#         yield i.upper()  # 함수의 반환 값을 바깥으로 전달


# fruits = ["apple", "pear", "grape", "pineapple", "orange"]
# for i in upper_generator(fruits):
#     print(i)

## yield from
# def number_generator():
#     x = [1, 2, 3]  # 반복 가능한 객체
#     yield from x


# for i in number_generator():
#     print(i)

## yield from에 제너레이터 객체 지정하기
# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1


# def three_generator():
#     yield from number_generator(3)


# for i in three_generator():
#     print(i)

# ## 제너레이터 표현식
x = (i for i in range(50) if i % 2 == 0)

print(x)

for i in x:
    print(i, end=" ")
