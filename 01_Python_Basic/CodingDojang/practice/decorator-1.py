# ## 데코레이터 사용하기기
# def trace(func):
#     def wrapper():
#         print(func.__name__, "Function Start")
#         func()  # 매개변수로 받은 함수를 호출
#         print(func.__name__, "Funtion End")

#     return wrapper  # wrapper 함수를 반환


# def deco2(func):
#     def wrapper():
#         print("deco 2")
#         func()

#     return wrapper


# @trace
# @deco2
# def hello():
#     print("hello")


# @trace
# @deco2
# def world():
#     print("world")


# hello()
# world()

## 매개변수와 반환값을 처리하는 데코레이터 만들기
# def trace(func):
#     def wrapper(a, b):  # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
#         r = func(a, b)  # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
#         print(f"{func.__name__}(a={a}, b={b}) -> {r}")
#         return r  # func의 반환값을 반환한다

#     return wrapper


# @trace
# def add(a, b):
#     return a + b


# print(add(10, 20))

## 가변 인수 함수 데코레이터
# def trace(func):
#     def wrapper(*args, **kwargs):  # 가변 인수 함수로 만들었다
#         r = func(*args, **kwargs)  # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
#         print(f"{func.__name__}(a={args}, b={kwargs}) -> {r}")
#         return r  # func의 반환값을 반환한다

#     return wrapper


# @trace
# def get_max(*args):
#     return max(args)


# @trace
# def get_min(**kwargs):
#     return min(kwargs.values())


# print(get_max(10, 20))
# print(get_min(x=10, y=20, z=30))

## 메서드에 데코레이터 사용하기
# def trace(func):
#     def wrapper(self, a, b):  # 호출할 함수는 인스턴스 메서드
#         r = func(self, a, b)  # self와 매개변수를 그대로 넣어준다
#         print(f"{func.__name__}(a={a}, b={b}) -> {r}")
#         return r  # func의 반환값을 반환한다

#     return wrapper


# class Calc:
#     @trace
#     def add(self, a, b):
#         return a + b


# c = Calc()
# print(c.add(10, 20))

## 매개변수가 있는 데코레이터 만들기
# def is_multiple(x):  # 데코레이터가 사용할 매개변수 지정
#     def real_decorator(func):  # 호출할 함수를 매개변수로 받는다
#         def wrapper(a, b):  # 호출할 함수의 매개변수와 똑같이 지정한다
#             r = func(a, b)  # func를 호출하고 반환값을 변수에 저장한다
#             if r % x == 0:
#                 print(f"The return value of {func.__name__} is multiple of {x}")
#             else:
#                 print(f"The return value of {func.__name__} is not multiple of {x}")
#             return r

#         return wrapper

#     return real_decorator


# # @is_multiple(3)  # @데코레이터(인수)
# # def add(a, b):
# #     return a + b


# # print(add(10, 20))
# # print(add(2, 5))

# ### 매개변수가 있는 데코레이터를 여러 개 지정하기
# @is_multiple(3)
# @is_multiple(7)
# def add(a, b):
#     return a + b


# add(10, 20)

## 클래스로 데코레이터 만들기
# class Trace:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self):
#         print(self.func.__name__, "Function Start")
#         self.func()
#         print(self.func.__name__, "Function End")


# @Trace
# def hello():
#     print("hello")


# hello()


# def bye():
#     print("bye")


# trace_bye = Trace(bye)  # 데코레이터에 호출할 함수를 넣어서 인스턴스 생성
# trace_bye()

# ## 클래스로 가변 인수 처리하는 데코레이터 만들기
# class Trace:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):  # 호출할 함수의 매개변수 처리
#         r = self.func(*args, **kwargs)
#         print(f"{self.func.__name__}(a={args}, b={kwargs}) -> {r}")
#         return r


# @Trace
# def add(a, b):
#     return a + b


# print(add(10, 20))
# print(add(a=10, b=20))


## 클래스로 매개변수가 있는 데코레이터 만들기
class IsMultiple:
    def __init__(self, x):  # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.x = x

    def __call__(self, func):  # 호출할 함수를 매개변수로 받는다
        def wrapper(a, b):  # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)
            if r % self.x == 0:
                print(f"The return value of {func.__name__} is multiple of {self.x}")
            else:
                print(
                    f"The return value of {func.__name__} is not multiple of {self.x}"
                )
            return r

        return wrapper


@IsMultiple(3)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))
