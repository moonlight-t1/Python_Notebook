## warlus operator ex 1
fresh_fruit = {"apple": 10, "banana": 4, "lemon": 0}


def make_lemonade(count):
    print(f"레몬은 {count}개 있습니다.")
    print("레모네이드를 만듭니다.")
    return 1


def out_of_stock():
    print("재고가 없습니다.")


count = fresh_fruit.get("lemon", 0)  # get method: 키가 없다면 지정한 디폴트 값 반환

# if count := fresh_fruit.get("lemon", 0):
#     make_lemonade(count)
# else:
#     out_of_stock()

## ex2
def make_cider(count):
    print(f"사과는 {count}개 있습니다.")
    print("사이다를 만듭니다.")
    return 1


# if (count := fresh_fruit.get("apple", 0)) >= 4:
#     make_cider(count)
# else:
#     out_of_stock()

## ex3
def slice_bananas(count):
    print(f"바나나 {count}를 슬라이스 합니다. 바나나가 {count * 2} 개가 됩니다.")
    return count * 2


class OutOfBanana(Exception):
    # print("바나나 에러")
    pass


def make_smoothies(count):
    if count < 4:
        raise OutOfBanana
    else:
        print(f"바나나 {count} 개로 스무디를 만듭니다")
        return "바나나 스무디"


pieces = 0
smoothies = ""
# if (count := fresh_fruit.get("banana", 0)) >= 2:
#     pieces = slice_bananas(count)
# else:
#     pieces = 0

# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBanana:
#     out_of_stock()


## ex04
to_enjoy = 0
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
    try:
        to_enjoy = make_smoothies(pieces)
    except OutOfBanana:
        out_of_stock()
elif (count := fresh_fruit.get("apple", 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get("lemon", 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "아무것도 없음"

print(to_enjoy)
