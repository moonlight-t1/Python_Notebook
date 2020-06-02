
class FishCakeMaker:
    def __init__(self, **kwargs):
        self._size = 10
        self._flavor = "팥"
        self._price = 100
        # kwargs 인자가 있다면 대체한다
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self._price = kwargs.get("price")

    def __del__(self):
        print("종료 되었습니다")

    def __str__(self):  # __str__()은 클래스가 print()에 의해 출력될 떄 실행된다.
        return "<class FishCakeMaker (size={}, price={}, falvor={})>".format(
            self._size, self._price, self._flavor)

    def __lt__(self, other):
        return self._price < other._price

    def __le__(self, other):
        return self._price <= other._price

    def __gt__(self, other):
        return self._price > other._price

    def __ge__(self, other):
        return self._price >= other._price

    def __eq__j(self, other):
        return self._price == other._price

    def __ne__(self, other):
        return self._price != other._price

    def show(self):
        print("=" * 30)
        print("붕어빵 종류 {}".format(self._flavor))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))


class MarketGoods(FishCakeMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)  # 부모 클래스의 생성자 호출
        self._market_price = self._price + margin

    def show(self):
        print(self._flavor, self._market_price)


if __name__ == "__main__":
    fish1 = MarketGoods(size=20, price=500)
    fish1.show()
