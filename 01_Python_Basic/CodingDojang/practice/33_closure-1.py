## global

x = 10


def foo():
    global x  # 전역 변수에 접근
    x += 10
    print(x)


foo()
print(x)


def foo():
    global y  # 전역 변수가 없을 때 함수 안에서 global을 사용하면 해당 변수는 전역 변수가 된다
    y = 20


## 함수 안에서 함수 만들기
def print_hello():
    hello = "Hello, world!"

    def print_message():
        print(hello)

    print_message()


print_hello()

## 지역 변수 변경하기
def A():
    x = 10

    def B():
        nonlocal x  # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20

    B()
    print(x)


## Closure
### 함수를 클로저 형태로 만들기
def calc():  # calc는 파라미터 없다
    a = 3
    b = 5

    def mul_add(x):  # 파라미터 받으면 여기로 들어간다
        return a * x + b  # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산

    return mul_add  # 함수 자체를 반환(이름만 반환해야 한다)


c = calc()
print(c(1), c(2), c(3), c(4), c(5))

"""
함수 calc가 끝났는데도 c는 calc의 지역 변수 a,b를 사용해서 계산하고 있다.
이렇게 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서
사용하는 함수를 클로저(closure)라 한다.
"""

### lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b


c = calc()
print(c(1), c(2), c(3), c(4), c(5))

### 클로저의 지역 변수 변경하기
def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total  # 클로저의 지역 변수 변경
        total = total + a * b + b
        print(total)

    return mul_add


c = calc()
c(1)
c(2)
c(3)
