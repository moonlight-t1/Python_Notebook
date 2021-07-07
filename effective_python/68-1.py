## pickle 사용
class GameState:
    def __init__(self):
        self.level = 0
        self.lives = 4


state = GameState()
state.level += 1  # 플레이어가 레벨을 깼다
state.lives -= 1  # 플레이어가 재시도해야 한다

print(state.__dict__)  # 객체의 속성 정보 확인

import pickle

state_path = "game_state.bin"

with open(state_path, "wb") as f:
    pickle.dump(state, f)

with open(state_path, "rb") as f:
    state_after = pickle.load(f)

print(state_after.__dict__)

"""
https://wikidocs.net/110788
"""
