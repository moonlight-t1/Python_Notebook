## 문자열 바꾸기
import re

# print(
#     re.sub("apple|orange", "fruit", "apple box orange tree")
# )  # apple 또는 orange를 tree로 바꾼다
# print(re.sub("[0-9]+", "n", "1 2 Fizz 4 Buzz Fizz 7 8"))  # 숫자만 찾아서 n으로 바꾼다

# ### 바꿀 문자열 대신 교체 함수 지정
# def multiple10(m):
#     n = int(m.group())  # 매칭된 문자열을 가져와서 정수로 변환
#     return str(n * 10)


# print(re.sub("[0-9]+", multiple10, "1 2 Fizz 4 Buzz Fizz 7 8"))

# print(re.sub("[0-9]+", lambda m: str(int(m.group()) * 10), "1 2 Fizz 4 Buzz Fizz 7 8"))

## 찾은 문자열을 결과에 다시 적용하기
### 그룹 번호 사용
print(re.sub("([a-z]+) ([0-9]+)", "\\2 \\1 \\2 \\1", "hello 1234"))
print(re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', "<\\2>\\3</\\2>", '{ "name": "james" }'))

### 그룹 이름
print(
    re.sub(
        '({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})',
        "<\\g<key>>\\g<value></\\g<key>>",
        '{ "name": "james" }',
    )
)

# ### raw 문자열 사용하기
print(re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', r"<\2>\3</\2>", '{ "name": "james" }'))

