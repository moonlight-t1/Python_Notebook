class Car(object):
    """
    Car Class
    Author : Me
    Date : 2021
    Description : Class, Static, Instatnce Method
    """

    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"

    # instance method
    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    def get_price(self):
        return f"Before Car Price -> Company : {self._company}, price : {self._details.get('price')}"

    def get_price_calc(self):
        return f"Before Car Price -> Company : {self._company}, price : {self._details.get('price') * Car.price_per_raise}"

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per  # assigning value to class variable
        return "Succeed! price increased."

    @staticmethod
    def is_bmw(inst):
        if inst._company == "BMW":
            return f"OK! This car is {inst._company}"
        return "Sorry. This car is not BMW"


if __name__ == "__main__":
    car1 = Car("Ferrari", {"Color": "White", "horsepower": 400, "price": 8000})
    car2 = Car("BMW", {"Color": "Black", "horsepower": 270, "price": 5000})
    car3 = Car("Audi", {"Color": "Silver", "horsepower": 300, "price": 6000})

    # car1.detail_info()
    # car2.detail_info()
    # print()

    print(car1.get_price())
    print(car2.get_price())
    print()

    # Car.price_per_raise = 1.2
    print(Car.raise_price(1.6))
    print()

    print(car1.get_price_calc())
    print(car2.get_price_calc())
    print()

    print(Car.is_bmw(car1))
    print(Car.is_bmw(car2))
    print()
