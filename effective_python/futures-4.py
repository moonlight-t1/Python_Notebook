import os
import time
from concurrent import futures

# 동시에 4개의 worker에게 일을 시켜서 각각 1부터 합을 구한다
WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 게산 메인 함수 - 누적 합계 함수(제너레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


# 진입점
def main():
    # Worker Count: worker 수를 10개 혹은 리스트의 원소 갯수 중 회소값으로 지정한다
    worker = min(10, len(WORK_LIST))  # pattern

    start_tm = time.time()  # 시작 시간

    # MultiProcess
    with futures.ThreadPoolExecutor(worker) as executor:
        result = executor.map(sum_generator, WORK_LIST)  # map -> 작업 순서 유지, 즉시 실행

    end_tm = time.time() - start_tm  # 종료 시간

    msg = "\n Result: {} Time : {:.2f}s"  # 출력 포멧
    print(msg.format(list(result), end_tm))  # 최종 결과


if __name__ == "__main__":
    main()
