class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # private attribute

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print("이제 {0}원 남았네요.".format(self.__wallet))


maria = Person("Maria", 20, "Seoul", 10000)
maria.pay(3000)
