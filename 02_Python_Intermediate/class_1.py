class Car:
    """
    Car Class
    Author : Seo
    Data : 2021.04.14
    """

    car_count = 0  # class varialbe

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "str : {} - {}".format(self._company, self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print(
            "Car Detail Info : {} {}".format(self._company, self._details.get("price"))
        )

    def __del__(self):
        Car.car_count -= 1


car1 = Car("Ferrari", {"Color": "White", "horsepower": 400, "price": 8000})
car2 = Car("BMW", {"Color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"Color": "Silver", "horsepower": 300, "price": 6000})

# list for object
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

for x in car_list:
    print(repr(x))
    # print(x)


# Check ID
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)  # comparison of value
print(car1 is car2)  # comparison of id

# check dir & __dict__
# it shows attributes of instance as list
print(dir(car1))
print(dir(car2))

print()
print()

# show key, value of name space
print(car1.__dict__)
print(car2.__dict__)

# print doc string
print(Car.__doc__)
print()

# execute
car1.detail_info()
car2.detail_info()

# comparison
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__))


print()

# instance variable (does not recommend)
print(car1._company, car2._company)
print(car2._company, car3._company)

print()
print()

# class variable
print(dir(car1))  # print class variable name

# access
print(car1.car_count)
print(car2.car_count)
print(Car.car_count)

print()
print()
