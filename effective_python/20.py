## 1. try / except
try:
    x = int(input("Enter num: "))
    y = 10 / x
    print(y)

except:  # 모든 예외 처리
    print("Exception")

# 2. 특정 예외만 처리하기
y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print("Cannot be divided by 0")
# except IndexError:
#     print("Wrong Index")

## 3. else: 예외가 발생하지 않았을 때 코드 실행
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except Exception as e:  # 모든 예외 출력
#     print("Exception:", e)
# else:  # try의 코드에서 예외가 발생하지 않았을 때 실행된다
#     print(y)

## 4. finally: 예외와는 상관없이 코드 실행
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except Exception as e:  # 모든 예외 출력
#     print("Exception:", e)
# else:  # try의 코드에서 예외가 발생하지 않았을 때 실행된다
#     print(y)
# finally:  # 예외와는 상관없이 항상 실행
#     print("Done")

## 5. raise: 예외 발생하기
# def add_num(num):
#     if num < 0:
#         raise Exception("Num must be greater than 0")
#     else:
#         return num + 1


# try:
#     x = int(input())
#     result = add_num(x)
# except Exception as e:
#     print("Exception: ", e)
# else:
#     print(result)

## 6. 현재 예외를 다시 발생시키기
# def three_multiple():
#     try:
#         x = int(input("Enter a multiple of 3: "))
#         if x % 3 != 0:
#             raise Exception("It is not a multiple of 3")
#         print(x)
#     except Exception as e:
#         print("three_multiple() Exception", e)
#         raise  # re-raise


# try:
#     three_multiple()
# except Exception as e:
#     print("Script File Exception.", e)

## 7. 예외 만들기
# class bcolors:
#     HEADER = "\033[95m"
#     OKBLUE = "\033[94m"
#     OKCYAN = "\033[96m"
#     OKGREEN = "\033[92m"
#     WARNING = "\033[93m"
#     ERROR = "\033[31m"
#     FAIL = "\033[91m"
#     ENDC = "\033[0m"
#     BOLD = "\033[1m"
#     UNDERLINE = "\033[4m"


# def print_error(error, e=None):
#     if e:
#         print(f"{bcolors.ERROR}{error} {e}{bcolors.ERROR}")
#     else:
#         print(f"{bcolors.ERROR}{error}{bcolors.ERROR}")


# class Calculator:
#     def __init__(self):
#         pass

#     def three_mutiple(self, x):
#         try:
#             x = int(input())
#             if x % 3 != 0:
#                 raise self.__NotThreeMutipleError
#             print(x)

#         except Exception as e:
#             print_error("ThreeMultipleException: ", e)

#     class __NotThreeMutipleError(Exception):  # Exception 상속
#         def __init__(self):
#             super().__init__("It is not a mutiple of 3")


# calc = Calculator()

# calc.three_mutiple(10)

## Docstring and Type Annotation
# def careful_divide(a: float, b: float) -> float:
#     """a를 b로 나눈다

#     Raises:
#         ValueError: b가 0이어서 나눗셈을 할 수 없을 때
#     """

#     try:
#         return a / b
#     except ZeroDivisionError:
#         raise ValueError


# x, y = 5, 0

# try:
#     result = careful_divide(x, y)
# except ValueError:
#     print("잘못된 입력입니다.")
# else:
#     print("결과는 %.1f 입니다" % result)

