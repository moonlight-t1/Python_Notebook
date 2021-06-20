class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[31m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_error(error, e=None):
    if e:
        print(f"{bcolors.ERROR}{error} {e}{bcolors.ERROR}")
    else:
        print(f"{bcolors.ERROR}{error}{bcolors.ERROR}")


class Calculator:
    def __init__(self):
        pass

    def three_mutiple(self, x):
        try:
            x = int(input())
            if x % 3 != 0:
                raise self.__NotThreeMutipleError
            print(x)

        except Exception as e:
            print_error("ThreeMultipleException: ", e)

    class __NotThreeMutipleError(Exception):  # Exception 상속
        def __init__(self):
            super().__init__("It is not a mutiple of 3")


calc = Calculator()

calc.three_mutiple(10)
