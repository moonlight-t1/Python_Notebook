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


# # try except
# try:
#     x = int(input("Enter num: "))
#     y = 10 / x
#     print(y)

# except:  # 모든 예외 처리
#     print("Exception")


# # 특정 예외만 처리하기
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print_error("Cannot be divided by 0")
# except IndexError:
#     print_error("Wrong Index")

# # 예외 메세지 받아오기
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print_error("Cannot be divided by 0:", e)
# except IndexError as e:
#     print_error("Wrong Index:", e)


# # 모든 예외 출력
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except Exception as e:  # 모든 예외 출력
#     print_error("Exception:", e)


# # 예외가 발생하지 않았을 때 코드 실행
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except Exception as e:  # 모든 예외 출력
#     print_error("Exception:", e)
# else: # try의 코드에서 예외가 발생하지 않았을 때 실행된다
#     print(y)

# # 예외와는 상관없이 항상 코드 실행하기
# y = [10, 20, 30]

# try:
#     index, x = map(int, input().split())
#     print(y[index] / x)
# except Exception as e:  # 모든 예외 출력
#     print_error("Exception:", e)
# else:  # try의 코드에서 예외가 발생하지 않았을 때 실행된다
#     print(y)
# finally: # 예외와는 상관없이 항상 실행
#     print("Done")

# # 예외 발생시키기
# def add_num(num):
#     if num < 0:
#         raise Exception("Num must be greater than 0")
#     else:
#         return num + 10


# try:
#     x = int(input())
#     result = add_num(x)
# except Exception as e:
#     print("Exception: ", e)
# else:
#     print(result)

# 현재 예외를 다시 발생시키기
def three_multiple():
    try:
        x = int(input("Enter a multiple of 3: "))
        if x % 3 != 0:
            raise Exception("It is not a multiple of 3")
        print(x)
    except Exception as e:
        print("three_multiple() Exception", e)
        raise


try:
    three_multiple()
except Exception as e:
    print("Script File Exception.", e)

## assert
x = int(input("Enter a multiple of 3: "))
assert x % 3 == 0, "It is not a multiple of 3"
print(x)
