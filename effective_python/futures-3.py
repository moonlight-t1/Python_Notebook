from time import time
from concurrent.futures import ThreadPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# 병렬성이 없으므로 이 함수를 순서대로 실행하면 시간이 선형적으로 증가
numbers = [
    (1963309, 2265973),
    (2030677, 3814172),
    (1551645, 2229620),
    (2039045, 2020802),
]
start = time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()
print("Took %.3f seconds" % (end - start))

