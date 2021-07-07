import pickle
import copyreg


class GameState:
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


def pickle_game_state(game_state):
    """
    GameState 객체를 받아서 copyreg 모듈이 
    용할 수 있는 튜플 파라미터로 변환해주는 도우미 함수
    
    인자 : GameStack 객체
    리턴값 : 언피클시 사용할 함수, 언피클 시 이 함수에 전달해야 하는 파라미터 정보
    """
    kwargs = game_state.__dict__  # 객체의 속성 정보
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    """
    직렬화한 데이터와 pickle_game_state가 돌려주는 튜플에 있는
    파라미터 정보를 인자로 받아서 그에 대응하는 GameState 객체를
    돌려준다
    """
    return GameState(**kwargs)  # 생성자를 감싼 함수


import copyreg

# 함수를 copyreg 내장 모듈에 등록
copyreg.pickle(GameState, pickle_game_state)

state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)


class GameState:
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic  # 추가한 필드


print("이전:", state.__dict__)
state_after = pickle.loads(serialized)  # 역직렬화
print("이후:", state_after.__dict__)

