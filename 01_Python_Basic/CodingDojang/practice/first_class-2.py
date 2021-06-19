def logger(msg):
    def log_message():
        print("Log: ", msg)

    return log_message


log_hi = logger("Hi")
print(log_hi)
log_hi()

del logger  # 글로벌 네임스페이스에서 logger 오브젝트를 지운다

# logger 오브젝트가 지워진 것을 확인한다
try:
    print(logger)
except NameError:
    print("NameError: logger doesn't exist.")

log_hi()  # loggerrㅏ 지워진 뒤에서 출력이 된다.
