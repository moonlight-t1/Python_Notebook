def outer_func_1():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func()  # 괄호


def outer_func_2():
    message = "Hello"

    def inner_func():
        print(message)

    return inner_func  # 괄호 x


# outer_func_1()  # Hi
# outer_func_2()  # 출력 x

my_func = outer_func_2()
# my_func()  # Hello
# my_func()  # Hello
# my_func()  # Hello

print(my_func)
print()
print(dir(my_func))
print()
print(type(my_func.__closure__))
print()
print(my_func.__closure__)
print()
print(my_func.__closure__[0])
print()
print(dir(my_func.__closure__[0]))
print()
print(my_func.__closure__[0].cell_contents)
