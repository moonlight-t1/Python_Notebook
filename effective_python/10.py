## warlus operator ex 1
fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5}


def make_lemonade(count):
    print(f"레몬은 {count}개 있습니다.")
    print("레모네이드를 만듭니다.")


def out_of_stock():
    print("재고가 없습니다.")


# count = fresh_fruit.get("lemon", 0)  # get method: 키가 없다면 지정한 디폴트 값 반환

if count := fresh_fruit.get("lemon", 0):
    make_lemonade(count)
else:
    out_of_stock()

## ex2
def make_cider(count):
    print(f"사과는 {count}개 있습니다.")
    print("사이다를 만듭니다.")


if (count := fresh_fruit.get("apple", 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

## ex3
def slice_banana(count):
    print(f"바나나 {count}를 슬라이스 합니다")


class OutOfBanana(Exception):
    pass


def make_smoothies(count):
    print(f"바나나 {count}개로 스무디를 만듭니다")

