## 기능 확장
import pickle

state_path = "game_state.bin"  # 이전 플레이


class GameState:
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0  # 새로운 필드


state = GameState()
serialized = pickle.dumps(state)
# print(serialized)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

with open(state_path, "rb") as f:
    state_after = pickle.load(f)  # 로드

print(state_after.__dict__)

assert isinstance(state_after, GameState)

"""
이런 동작은 pickle 모듈이 동작할 때 생기는 부작용입니다. 
pickle을 사용하는 주 용도는 객체를 쉽게 직렬화하는 것입니다. 
pickle을 단순한 용도 이상으로 사용하자마자 모듈의 기능이 놀랍게 망가집니다. 

내장 모듈 copyreg를 이용하면 이 문제를 간단히 해결할 수 있습니다. 
copyreg모듈로 파이썬 객체를 직렬화할 함수를 등록하여 pickle의 동작을 제어하고 
pickle을 더 신뢰할 수 있게 만들 수 있습니다.


https://docs.python.org/ko/3/library/copyreg.html
"""
