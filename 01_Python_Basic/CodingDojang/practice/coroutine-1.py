## 코루틴에 값 보내기
# def number_coroutine():
#     while True:  # 코루틴을 계속 유지하기 위해 무한 루프 사용
#         x = yield  # 코루틴 바깥에서 값을 받아온다
#         x += 10
#         print(x)


# co = number_coroutine()
# next(co)  # 코루틴 안의 yield까지 코드 실행(최초 실행)

# co.send(1)  # 코루틴에 숫자 1을 보낸다
# co.send(2)  # 코루틴에 숫자 1을 보낸다
# co.send(3)  # 코루틴에 숫자 1을 보낸다


## 코루틴에서 바깥으로 값을 전달하기
# def sum_coroutine():
#     total = 0  # 바깥으로 보낼값
#     while True:
#         x = yield total  # 코루틴 바깥에서 값을 받아오면서(x) 바깥으로 값을 전달(total)
#         total += x


# co = sum_coroutine()
# print(next(co))  # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력

# print(co.send(1))  # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
# print(co.send(2))  # 2: 코루틴에 숫자 2을 보내고 코루틴에서 나온 값 출력
# print(co.send(3))  # 3: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

# ## GeneratorExit 예외 처리하기
# def number_coroutine():
#     try:
#         while True:
#             x = yield
#             print(x, end=" ")
#     except GeneratorExit: # 코루틴이 종료 될 때 GeneratorExit 예외 발생
#         print()
#         print("Finished Coroutine")


# co = number_coroutine()
# next(co)

# for i in range(20):
#     co.send(i)

# co.close() # 코루틴 종료

## 코루틴 안에서 예외 발생시키기
# def sum_coroutine():
#     try:
#         total = 0
#         while True:
#             x = yield
#             total += x
#     except RuntimeError as e:
#         print(e)
#         yield total  # 코루틴 바깥으로 값 전달


# co = sum_coroutine()
# next(co)

# for i in range(20):
#     co.send(i)

# print(co.throw(RuntimeError, "Finished Coroutine with Exception"))

## 하위 코루틴의 반환값 가져오기
# def accumulate():
#     total = 0
#     while True:
#         x = yield  # 코루틴 바깥에서 값을 받아온다
#         if x is None:  # 받아온 값이 None이면
#             return total  # 합계를 반환
#         total += x


# def sum_coroutine():
#     while True:
#         total = yield from accumulate()  # accumulate의 반환값을 가져옴
#         print(total)


# co = sum_coroutine()
# next(co)

# for i in range(1, 11):
#     co.send(i)  # 코루틴 accumulate에 숫자를 보낸다
# co.send(None)  # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

# for i in range(1, 101):
#     co.send(i)  # 코루틴 accumulate에 숫자를 보낸다
# co.send(None)  # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄


## StopIteration 예외 발생시키기(3.6 이하)

## 코루틴의 yield from으로 값을 발생 시키기
def number_coroutine():
    x = None
    while True:
        x = yield x  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x == 3:
            return x


def print_coroutine():
    while True:
        x = yield from number_coroutine()  # 하위 코루틴의 yield에 지정된 값을 다시 바깥으로 전달
        print("print_coroutine: ", x)


co = print_coroutine()
next(co)

x = co.send(1)  # number_coroutine으로 1을 보낸다
print(x)  # 1: number_corouine의 yield에서 바깥으로 전달한 값
x = co.send(2)  # number_coroutine으로 1을 보낸다
print(x)  # 2: number_corouine의 yield에서 바깥으로 전달한 값
co.send(3)  # 3을 보내서 반환값을 출력하도록 만든다

