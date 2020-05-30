import time
from functools import wraps
"""
데코레이터
이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

파이썬에서 함수는 일급객체
클로저 사용
함수내 함수를 정의할 수 있음
"""


# def outer_function(msg):
#     def inner_function():
#         return "난 내부 함수인데 {} 메세지를 받았어".format(msg)
#     return inner_function


# c = outer_function("헬로")
# # print(c())
# # print(dir(c()))
# # print(type(c.__closure__))
# # print(dir(c.__closure__[0]))
# print(c.__closure__[0].cell_contents)

""" 클로저 """


# def test():
#     start_time = time.time()
#     for i in range(5):
#         time.sleep(0.1)
#     end_time = time.time() - start_time
#     print("함수 동작 시간: {}".format(end_time))


# test()

# 클로저 함수


# import time
# def time_checker(func):
#     def inner_function(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print("함수 {} 동작시간: {}".format(func.__name__, end_time-start_time))
#         return result
#     return inner_function


# @time_checker
# def test1():
#     for i in range(5):
#         time.sleep(0.1)


# @time_checker
# def test2():
#     for i in range(3):
#         time.sleep(0.1)


# test1()
# test2()

""" 데코레이터 2 """


# def login_required(func):
#     @wraps(func)
#     def inner_function(*args, **kwargs):
#         if not kwargs.get("is_login"):
#             print("로그인이 되지 않아 수행하지 못합니다.")
#             return "로그인이 필요한 페이지입니다."
#         return func(*args, **kwargs)
#     return inner_function


# @login_required
# def login():
#     """
#     로그인 테스트 함수 입니다
#     """
#     print("안녕")


# print(login.__name__)
# print(login.__doc__)


# login()

""" 데코레이터 3"""


def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}>{}</{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator


@add_tag("html")
def test(msg):
    return msg + " 팀장님"


print(test("이세영"))
