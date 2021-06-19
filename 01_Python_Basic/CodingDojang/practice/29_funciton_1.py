## 함수에서 값을 여러 개 반환하기기
def add_sub(a, b):
    return a + b, a - b  # 튜플이 반환된다


x, y = add_sub(20, 10)  # unpacking
print(x, y)

## 언패킹 사용하기기
def print_nums(*nums):
    for num in nums:
        print(num, end=" ")


nums = [10, 20, 30, 40, 50]
print_nums(nums)
print()
print_nums(*[10, 20, 30])

## 고정 인수와 가변 인수를 함께 사용하기
def print_numbers(str, *nums):
    def print_nums(nums):
        for num in nums:
            print(num + 10, end=" ")

    print(str, ":", end="")
    print_nums(nums)


print_numbers("integers", *[10, 20, 30])
print()
## 키워드 인자 사용하기
def personal_info(name, age, address):
    print("name: ", name)
    print("age : ", age)
    print("address : ", address)


personal_info(age=10, name="Andrew", address="Seoul")

x = {"name": "Alex", "age": 30, "address": "New York"}
personal_info(**x)

## 키워드 인수르 사용하는 가변 인수 함수 만들기
def peronal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ": ", arg, sep=" ")


peronal_info(**x)


def personal_info_kw(**kwargs):
    if "name" in kwargs:
        print("his name: ", kwargs["name"])
    if "age" in kwargs:
        print("his age: ", kwargs["age"])
    if "address" in kwargs:
        print("his address: ", kwargs["address"])


personal_info_kw(**x)

## 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=":", end="")

