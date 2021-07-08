# aiohttp 권장
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import nest_asyncio

nest_asyncio.apply()

# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장(예 : 게시판성 커뮤니티)
urls = [
    "http://daum.net",
    "https://naver.com",
    "http://mlbpark.donga.com/",
    "https://tistory.com",
    "https://wemakeprice.com/",
]

# fetch 함수
async def fetch(url, executor):
    # 쓰레드명 출력
    print(
        "Thread Name :", threading.current_thread().getName(), "Start", url
    )  # 디버깅용 코드

    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    print("Thread Name :", threading.current_thread().getName(), "Done", url)  # 디버깅용 코드

    # 결과 반환
    return res.read()[0:5]  # 각 사이트의 시작하는 5글자만 가져온다


# 실행
res = await loop.run_in_executor(executor, urlopen, url)

# main 함수
async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    # 결과 취합
    rst = await asyncio.gather(*futures)

    print()
    print("Result : ", rst)

  # future 객체 모아서 gather에서 실행
  futures = [
      asyncio.ensure_future(fetch(url, executor)) for url in urls
  ]