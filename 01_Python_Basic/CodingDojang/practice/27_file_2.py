## 반복문으로 문자열 여러 줄을 파일에 쓰기
with open("Hello.txt", "w") as file:
    for i in range(3):
        file.write("Hello, world! {0}\n".format(i))

## 리스트에 들어 있는 문자열 파일에 쓰기기
# lines = ["Hello\n", "World\n", "Python\n"]

# with open("Hello.txt", "w") as file:
#     file.writelines(lines)


## 파일의 내용을 한 줄씩 리스트로 가져오기
with open("hello.txt", "r") as file:
    lines = file.readlines()

print(lines)

## 파일의 내용을 한 줄씩 읽기
with open("Hello.txt", "r") as file:
    line = None
    while line != "":
        line = file.readline()
        print(line.strip("\n"))

## for 반복문으로 파일의 내용을 줄 단위로 읽기
with open("hello.txt", "r") as file:
    for line in file:
        print(line.strip("\n"))

## 파일 객체는 이터레이터
file = open("hello.txt", "r")

a, b, c = file  # unpacking
print(a, b, c)


file.close()
