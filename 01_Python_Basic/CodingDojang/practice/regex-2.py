## 범위 판단하기
import re

print(re.match("[0-9]*", "1234"))  # 숫자가 0개 이상 있는지
print(re.match("[0-9]+", "1234"))  # 숫자가 1개 이상 있는지
print(re.match("[0-9]+", "abcd"))  # 숫자가 1개 이상 있는지
print()

print(re.match("a*b", "b"))  # a가 0개 이상 있는지
print(re.match("a+b", "b"))  # a가 1개 이상 있는지
print(re.match("a*b", "aab"))  # a가 0개 이상 있는지
print(re.match("a+b", "aab"))  # a가 1개 이상 있는지
print()

## 문자가 한 개만 있는지 판단하기
print(re.match("abc?d", "abd"))  # ? 앞에 c가 0개 이상 있는지
print(re.match("ab[0-9]?c", "abcd"))  # 숫자가 0개 이상 있는지
print(re.match("ab.d", "abxd"))  # . 위치에 문자가 1개 있는지
print()

## 문자 개수 판단하기
print(re.match("h{3}", "hhhello"))  # 문자가 몇 개 있는지
print(re.match("hello{3}", "hellohellohelloworld"))  # 문자열이 몇 개 있는지
print()

### 휴대전화 번호 형식이 맞는지
print(re.match("[0-9]{3}-[0-9]{4}-[0-9]{4}", "010-1000-1000"))  # 숫자 3-4-4 패턴
print(re.match("[0-9]{3}-[0-9]{4}-[0-9]{4}", "010-1000-100"))  # 숫자 3-4-4 패턴
print()
print(
    re.match("[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}", "02-100-1000")
)  # 숫자 2개 혹은 3개 / 3개 혹은 4개
print(
    re.match("[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}", "02-10-1000")
)  # 숫자 2개 혹은 3개 / 3개 혹은 4개

print()

## 숫자와 영문 문자를 조합해서 판단하기
print(re.match("[a-zA-Z0-9]+", "Hello1234"))  # 소문자, 대문자, 숫자가 1개 이상 있는지
print(re.match("[A-Z0-9]+", "hello"))  # 대문자, 숫자가 1개 이상 있는지
print(re.match("[가-힣]+", "홍길동"))  # 한글
print()

## 특정 문자 범위에 포함되지 않는지 판단하기
print(re.match("[^A-Z]+", "Hello"))  # 대문자가 포함되지 않는지
print(re.match("[^A-Z]+", "hello"))  # 대문자가 포함되지 않는지
print()

## 헷갈림 주의
print(re.search("^[A-Z]+", "Hello"))  # 대문자로 시작하는지
print(re.search("[0-9]+$", "Hello1234"))  # 숫자로 끝나는지
print()

## 특수 문자 판단하기
print(re.search("\*+", "1**2"))  # *이 1개 이상 있는지 확인
print(re.match("[$()a-zA-Z0-9]", "$(document)"))  # $, (, ), 와 문자 숫자가 있는지
print()


print(re.match("\d+", "1234"))  # 모든 숫자
print(re.match("\D+", "Hello"))  # 숫자를 제외한 모든 문자
print(re.match("\w+", "Hello_1234"))  # 영문 대소문자, 숫자, 밑줄문자
print(re.match("\W+", "(:)"))  # 영문 대소문자, 숫자 밑줄문자를 제외한 모든 문자
print()

## 공백 처리하기
print(re.match("[a-zA-Z0-9 ]+", "Hello 1234"))  # ' '로 공백 표현
print(re.match("[a-zA-Z0-9\s]+", "Hello 1234"))  # \s로 공백 표현
print()

## 같은 정규 표현식 패턴을 자주 사용할 때 - compile
p = re.compile("[0-9]+")
print(p.match("1234"))
print(p.search("hello"))

