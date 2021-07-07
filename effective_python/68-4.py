import pickle
import copyreg


# 객체의 필드 삭제한 경우
class GameState:
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic


# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# pickle.loads(serialized)


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs["version"] = 2  # 버전 추가
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    version = kwargs.pop("version", 1)
    if version == 1:
        del kwargs["lives"]  # del
    return GameState(**kwargs)


copyreg.pickle(GameState, pickle_game_state)

state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)


print("이전:", state.__dict__)
state_after = pickle.loads(serialized)
print("이후:", state_after.__dict__)

