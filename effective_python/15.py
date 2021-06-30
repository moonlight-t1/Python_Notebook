baby_names = {"cat": "kitten", "dog": "puppy", "bird": "birdy"}


print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_func(goose="gosling", kangaroo="joey")

## class
class MyClass:
    def __init__(self):
        self.alligator = "hatchling"
        self.elephant = "calf"


a = MyClass()
for key, value in a.__dict__.items():  # 인스턴스 필드를 대입한 순서가 __dict__에 반영
    print("%s = %s" % (key, value))

# ##
votes = {"otter": 1281, "polar bear": 587, "fox": 863}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)  # dictionary의 value값을 기준으로 정렬
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winer(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winer(ranks)
print(winner)

## orderedDict
