# Chapter05-03
# 파이썬 심화
# 클로저 심화


# 클로저(Closure) 사용
def closure_ex1():
    series = []  # 자유 변수(free variable)

    # 클로저 영역
    def averager(v):
        # series = [] # 주석 해제 후 확인
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    # 함수를 리턴
    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()


# function inspection

# 함수의 dir
print(dir(avg_closure1))
print()
# avg_closure의 __code__
print(dir(avg_closure1.__code__))
print()
# co_freevars(자유변수)
print(avg_closure1.__code__.co_freevars)
print()
# 클로저의 [0]
print(dir(avg_closure1.__closure__[0]))
print()
# 클로저[0]의 cell_contents
print(avg_closure1.__closure__[0].cell_contents)

print()
print()


# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1  # cnt = cnt + 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()

# print(avg_closure2(15)) # 예외


# Nonlocal -> Free variable
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()
