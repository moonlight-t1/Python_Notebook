## 문자열 바꾸기
a = "Hello, World!"
b = a.replace("Hello", "Python")  # 바뀐 결과 반환
print(b)


## 문자 바꾸기
table = str.maketrans("aeiou", "12345")
str = "apple"
str = str.translate(table)
print(str)

## 문자열 분리하기
str = "apple pear graph pineapple orange".split()  # 공백 기준
print(str)

str = "apple, pear, graph, pineapple, orange".split(", ")
print(str)

## 구분자 문자열과 문자열 리스트 연결하기
str = " ".join(["1990", "01", "01"])
print(str)

str = ":".join(["1990", "01", "01"])
print(str)

## upper()
print("hello".upper())

## lower()
print("HELLO".lower())

## strip
str = "    Python    "
print(str.lstrip())  # lstrip
print(str.rstrip())  # rstrip
print(str.strip())  # strip


str = "....Python...."
print(str.lstrip("."))  # lstrip
print(str.rstrip("."))  # rstrip
print(str.strip("."))  # strip

## 구두점을 간단하게 삭제하기
import string

str = ", python."
s = str.strip(string.punctuation)
print(s)

s = str.strip(string.punctuation + " ")  # 공백까지 삭제
print(s)

s = s.strip(string.punctuation).strip()  # 메서드 체이닝
print(s)

print(string.punctuation)

## 문자열 정렬
s = "python".ljust(10)  # 왼쪽 정렬
print(s)

s = "python".rjust(10)  # 왼쪽 정렬
print(s)

s = "python".center(10)  # 왼쪽 정렬
print(s)

## 문자열 채우기
print("35".zfill(4))
print("3.5".zfill(6))
print("hello".zfill(10))

## 문자열 위치 찾기
s = "apple pineapple"
print(s.find("pl"))
print(s.find("xy"))

print(s.rfind("pl"))  # 오른쪽에서부터 찾기
print(s.rfind("xy"))  # 오른쪽에서부터 찾기

## index로 문자열 위치 찾기
print(s.index("pl"))
print(s.rindex("pl"))

## 문자열 개수 세기
print(s.count("pl"))

