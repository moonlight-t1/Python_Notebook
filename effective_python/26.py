from functools import wraps
import pickle


def trace(func):
    @wraps(func)  # 추가
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r}, {kwargs!r}) " f"-> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n):
    """
    n번째 피보나치 수를 반환한다
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(4)
print(help(fibonacci))  # 피보나치의 독스트링 출력
print(pickle.dumps(fibonacci))  # pickle
