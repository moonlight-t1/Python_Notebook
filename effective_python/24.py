from time import sleep
from datetime import datetime


def log(message, when=None):
    """메시지와 타임스탬프를 로그에 남긴다

    Args:
        message: 출력할 메시지
        when: 메시지가 발생한 시각(datetime)
            디폴트 값은 현재 시간이다
    """
    if when is None:
        when = datetime.now()  # 여기다 datetime.now()를 넣어준다
    print(f"{when}: {message}")


log("hi")
sleep(0.1)
log("hello")


## 2
import json


def decode(data, default=None):
    """문자열로부터 JSON 데이터를 읽어온다

    Args:
        data: 디코딩할 JSON 데이터
        default: 디코딩 실패 시 반환할 값이다.
            디폴트 값은 빈 딕셔너리이다
    """

    try:
        return json.loads(data)  # json 디코딩
    except ValueError:
        if default is None:  # 디코딩에 실패하면 빈 딕셔너리 반환
            default = {}
        return default


foo = decode("잘못된 데이터")
foo["stuff"] = 5
foo["hello"] = 2

bar = decode("또 잘못된 데이터")
bar["meep"] = 1
bar["bye"] = 3
print("Foo: ", foo)
print("Bar: ", bar)
assert foo is not bar


## 3
from typing import Optional


def log_typed(message: str, when: Optional[datetime] = None) -> None:
    """메시지와 타임스탬프를 로그에 남긴다
    
    Args:
        message: 출력할 메시지
        when: 메시지가 발생한 시각(datetime)
            디폴트 값은 현재 시간이다
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


log_typed("hello", "s")
log_typed("hello")
# print(hello)

