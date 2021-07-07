import pickle
import copyreg


class BetterGameState:
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs["version"] = 2  # 버전 추가
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    version = kwargs.pop("version", 1)
    if version == 1:
        del kwargs["lives"]  # del
    return BetterGameState(**kwargs)


state = BetterGameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)


# pickle 사용
pickle.loads(serialized)

print(serialized)

# copyreg 사용
# unpickle _game_state에 대한 임포트 경로가 인코딩된다
copyreg.pickle(BetterGameState, pickle_game_state)

state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized)
