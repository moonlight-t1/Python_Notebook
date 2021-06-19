class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"{bcolors.OKGREEN}Hello. I am {self.name}.{bcolors.ENDC}")


class PeakyBlinders(Person):
    def __init__(self, name, weapon):
        super().__init__(name)  # 기반 클래스의 __init__ 메서드 호출
        self.__weapon = weapon

    def attack(self):
        print(
            f"{bcolors.WARNING}{self.name} attacks with {self.__weapon}.{bcolors.ENDC}"
        )

    def greeting(self):  # method overriding
        super().greeting()  # 기반 클래스의 메서드 호출
        print(f"{bcolors.OKCYAN}We are Peaky fxxking Blinders.{bcolors.ENDC}")


class PeakyList:
    def __init__(self):
        self.__person_list = []

    def append_person(self, person):
        self.__person_list.append(person)

    def get_list(self):
        return self.__person_list


thomas = PeakyBlinders("Thomas Shelby", "Pistol")
thomas.greeting()
thomas.attack()

# polly = Person("Polly Grey", "Aunt", "Birmingham", 500)
# arthur = Person("Arthur Shelby", "Action Leader", "Birmingham", 700)

# print(issubclass(PeakyBlinders, Person))

