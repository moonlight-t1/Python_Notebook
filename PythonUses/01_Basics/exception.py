""" 파이썬 예외 처리 try / except """

try:
    val = "10.5"
    n = int(val)

# except ValueError as e: # value error 일 때 catch
    # print("오류 발생 {}".format(e))

except Exception as e:
    print("오류 발생 {}".format(e))

""" try except finlly """
try:
    n = "10.5"
    n = int(n)
except:
    print("오류 발생")
else:  # 오류 없을시 실행
    print("정상동작")
finally:  # 오류 상관없이 실행
    print("finally")
