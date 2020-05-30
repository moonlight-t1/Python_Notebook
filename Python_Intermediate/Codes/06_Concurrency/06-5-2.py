# Chapter06-05
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행 , 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed


WORK_LIST = [
    100000000,
    100000,
    10000,
    1000000,
]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제레네이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))


# as_completed
def main():
    worker = min(10, len(WORK_LIST))  # Worker 카운트
    start_tm = time.time()  # 시작 시간
    futures_list = []  # future

    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환(아직 실행되지 않는다. 미래에 할일을 반환할 뿐이다)
            future = excutor.submit(sum_generator, work)

            # 스케쥴링(4개의 일을 담는다)
            futures_list.append(future)

            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))

        print()

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()  # 결과
            done = future.done()  # 끝났는지
            cancelled = future.cancelled  # 취소 됐는지

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))  # 완료
            print('Future Cancelled : {}'.format(cancelled))  # 취소
            print()

    end_tm = time.time() - start_tm  # 종료 시간
    msg = '\n Time : {:.2f}s'  # 출력 포맷
    print(msg.format(end_tm))  # 최종 결과 출력


# 실행
if __name__ == '__main__':
    main()
