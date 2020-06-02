""" 사용자 함수 """

# c = 10


# def add(a, b):
#     global c  # 전역변수 c를 사용하겠다고 선언
#     c = a + b
#     return c


# b = add(1, 10)
# print(b, c)


""" 사용자 함수 2"""


# def get_input_user(msg, casting=int):  # casting의 기본값으로 int
#     '''
#     사용자에게 msg를 출력하고 casting 현태를 확인하여
#     입력된 값을 리턴한다.

#     Args:
#         meg (str) : input 시 출력할 문구
#         casting (class) : 사용자에게 입력 받은 값의 자료형

#     Returns:
#         user (casting-value) : 사용자에게 입력받은 값
#     '''
#     while True:
#         try:
#             user = casting(input(msg))
#             return user
#         except:
#             continue
#     return user


# user = get_input_user("사용자 이름을 입력하세요. > ", str)
# age = get_input_user("사용자 나이를 입력하세요. > ")

# print(user, age)

""" 소수 판별 """


# def is_prime_number(num):
#     prime_lists = [False, False] + [True] * (num - 1)
#     primes = []
#     for i in range(2, num + 1):
#         if prime_lists[i]:
#             for j in range(2 * i, num + 1, i):
#                 prime_lists[j] = False
#     primes = [i for i in range(2, num + 1) if prime_lists[i] == True]

#     if num in primes:
#         return True
#     else:
#         return False


# num = get_input_user("2 이상이 숫자를 입력하세요> ", int)
# if is_prime_number(num):
#     print("{} 는 소수 입니다.".format(num))
# else:
#     print("{} 는 소수가 아닙니다.".format(num))


""" Immutable(Call by value) """


# def test1(num):
#     num += 10
#     print(num)


# def test2(lists):  # mutable
#     lists.append("AAAA")
#     print(lists)


# a = 50
# test1(a)
# print(a)

# b = []
# b.append("1234")
# test2(b)
# print(b)

""" 인자 언패킹 """


# def save_winner(*args):
#     print(args)
#     print(args[0])


# save_winner("박은빈")
# save_winner("박은빈", "이세영")
# save_winner("박은빈", "이세영", "송지원")


# def air_line(departure, **kwargs):
#     print('출발지는 : ', departure)
#     print('도착지는 : ', kwargs['arrival'])
#     print('비행시간은 : ', kwargs['flighttime'])


# air_line(**{'departure': '인천', 'arrival': '멜버른', 'flighttime': '11시간'})

""" 함수를 변수에 담을 수 있다 """


# def hi():
#     print("Hello")


# hello = hi  # 변수에 담을 때 괄호 생략
# hello()
# print(type(hello))


# def add(a, b):
#     return a + b


# def cal(func, a, b):
#     print("결과 {}".format(func(a, b)))


# cal(add, 1, 5)

""" 함수 안에 함수를 선언할 수 있다 """


def outer_function(func):
    def inner_function(*args, **kwargs):
        print("함수명 : {}".format(func.__name__))
        print("args : {}".format(args))
        print("kwargs : {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result : {}".format(result))
        return result
    return inner_function


def add(a, b):
    return a + b


f = outer_function(add)
f(10, 20)
