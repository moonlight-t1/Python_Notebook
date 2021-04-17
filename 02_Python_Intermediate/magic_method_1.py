class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # string
    def __str__(self):
        return f"Fruit Class Info : {self._name}, {self._price}"

    # add
    def __add__(self, x):
        print("Called >> __add__ Method.")
        return self._price + x._price

    # subtract
    def __sub__(self, x):
        print("Called >> __sub__ Method.")
        return self._price - x._price

    # greater equal
    def __ge__(self, x):
        print("Called >> __ge__ Method.")
        if self._price >= x._price:
            return True
        else:
            return False

    # lesser equal
    def __le__(self, x):
        print("Called >> __le__ Method.")
        if self._price <= x._price:
            return True
        else:
            return False


s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# not using magic method
print(s1._price + s2._price)

# using magic method
print(s1 + s2)

# magic method
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s2)
print(s1)
print(s2)