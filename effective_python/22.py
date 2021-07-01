## positional argument(위치 인자)
## 위치 인자 = 가변 인자 = 스타 인자
# def log(message, *values):
#     if not values:
#         print(message)
#     else:
#         value_str = ", ".join(str(x) for x in values)
#         print(f"{message}: {value_str}")


# log("numbers", 1, 2, 3)

# favorites = [7, 33, 99]  # sequence(list)
# log("favorite number ", *favorites)

## keyword argument
d = {"Python": 10, "C++": 20}

x = {"name": "홍길동", "age": 30, "address": "서울시 용산구 이촌동"}


# def personal_info(**kwargs):
#     if "name" in kwargs:  # in으로 딕셔너리 안에 특정 키가 있는지 확인
#         print("이름: ", kwargs["name"])
#     if "age" in kwargs:
#         print("나이: ", kwargs["age"])
#     if "address" in kwargs:
#         print("주소: ", kwargs["address"])


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_info(**d)
print_info(**x)

