## 특정 클래스의 인스턴스인지 확인


class Person:
    # __slots__ = ["name", "age", "address"]  # 속성 추가 제한

    # public class attributes
    bag = []  # 클래스 속성(모든 인스턴스가 공유)
    item_num = 0

    # private attributes
    __item_limit = 1  # 비공개 클래스 속성
    __person_count = 0

    def __init__(self, name, roll, address, wallet):
        self.name = name
        self.address = address
        self.age = roll
        self.__wallet = wallet  # 비공개 속성
        Person.__person_count += 1  # 비공개 클래스 속성

    def greeting(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old.")

    def pay(self, amount):
        self.__wallet -= amount
        print(f"Money left : {self.__wallet}")

    def put_bag(self, stuff):
        if Person.item_num <= Person.__item_limit:
            Person.bag.append(stuff)
            Person.item_num += 1
        else:
            print("The bag is full.")

    @staticmethod
    def peaky_blinders():  # static method는 외부 상태에 영향을 끼치지 않는 순수(pure) 함수이다
        print("We are fxxking peaky blinders.")

    @classmethod
    def print_count(cls):  # class method는 메서드 안에서 클래스 속성, 클래스 메서드에 접근할 때 사용한다
        print(f"There are {Person.__person_count} Peaky Blinders.")


thomas = Person("Thomas Shelby", "Boss", "Birmingham", 1000)
polly = Person("Polly Grey", "Aunt", "Birmingham", 500)
arthur = Person("Arthur Shelby", "Action Leader", "Birmingham", 700)

thomas.put_bag("gun")
polly.put_bag("pistol")
arthur.put_bag("rocket launcher")

print(Person.bag)
Person.peaky_blinders()
Person.print_count()

# print(Person.__dict__)

# print(isinstance(thomas, Person))
# james.hobby = "fishing"  # 다른 속성 추가


# print(james.hobby)

