## 소수 제너레이터 만들기
def prime_number_generator(start, stop):
    n = start
    while n < stop:
        flag = 0
        for i in range(2, n // 2):
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            yield n
        n += 1


## 혹은 다음과 같이 만들 수 있다.
def prime_number_generator2(start, stop):
    for n in range(start, stop):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
        if is_prime == True:
            yield n


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=" ")

