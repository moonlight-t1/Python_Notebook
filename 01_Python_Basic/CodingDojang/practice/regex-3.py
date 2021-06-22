## 그룹 사용하기
import re

m = re.match("([0-9]+) ([0-9]+)", "10 295")
print(m.group(1))
print(m.group(2))
print(m.group())
print(m.group(0))
print()
print(m.groups())

### 그룹 이름 짓기
m = re.match("(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)", "print(1234)")
# m = re.match("(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)", "print(1234)")
print(m.group("func"))
print(m.group("arg"))


## 패턴에 매칭되는 모든 문자열 가져오기
print(re.findall("[0-9]+", "1 2 Fizz 4 Buzz Fizz 7 8"))


## *, +와 그룹 활용하기
print(re.match("[a-z]+(.[a-z]+)*$", "hello.world"))  # 점과 영문 소문자가 한 개 이상 있는지 판단
print(re.match("[a-z]+(.[a-z]+)*$", "hello.1234"))
print(re.match("[a-z]+(.[a-z]+)*$", "hello"))
