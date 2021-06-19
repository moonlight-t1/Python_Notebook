## 파일에 문자열 쓰기
# file = open("hello.txt", "w")  # open 함수로 파일을 열어 파일 객체(file object)를 얻는다.

# file.write("Hello, world!")
# file.close()


## 파일에서 문자열 읽기
file = open("hello.txt", "r")
s = file.read()  # 모든 문자들이 여기에 담긴다.

print(s)
file.close()

## 자동으로 파일 객체 닫기
with open("hello.txt", "r") as file:
    s = file.reaD()
    print(s)
