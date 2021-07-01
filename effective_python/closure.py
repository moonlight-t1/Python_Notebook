def outer_func_1():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func()  # 괄호


# closure
def outer_func_2():
    message = "Hello"

    def inner_func():
        print(message)

    return inner_func  # 괄호 x


my_func2 = outer_func_1()  # Hi
# # outer_func_2()  # 출력 x

my_func = outer_func_2()
# # my_func()  # Hello
# # my_func()  # Hello
# # my_func()  # Hello

# print(my_func)  # 1
# print()
print(dir(my_func))  # 2
print(dir(my_func2))
# print()
# print(type(my_func.__closure__))  # 3
# print()
# print(my_func.__closure__)  # 4
# print()
# print(my_func.__closure__[0])  # 5
# print()
# print(dir(my_func.__closure__[0]))  # 6
# print()
# print(my_func.__closure__[0].cell_contents)  # 7


def countdown(n):
    tmp = n  # 인자로 받은 숫자 저장

    def down():
        nonlocal tmp  # 지역변수 tmp를 수정하기 위한 nonlocal
        n = tmp
        tmp -= 1
        return n

    return down


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=" ")
