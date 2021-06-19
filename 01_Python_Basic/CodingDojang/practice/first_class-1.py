def square(x):
    return x * x


def cube(x):
    return x * x * x


def quad(x):
    return x * x * x * x


print(square(5))

f = square  # 변수에 함수를 할당

print(square)
print(f)
print(f(5))  # 변수를 이용하여 함수 호출


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))  # square 함수 호출
    return result


num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)

print(squares)
print(cubes)
print(quads)
