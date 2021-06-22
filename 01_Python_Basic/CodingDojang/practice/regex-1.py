## 문자열 판단하기

import re

print(re.match("Hello", "Hello, world!"))  # 매칭되는 문자열이 있으므로 정규표현식 매치 객체가 반환된다.
print(re.match("Python", "Hello, world!"))


## 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
print(re.search("^Hello", "Hello, world!"))  # ^: 문자열이 맨 앞에 오는지 판단
print(re.search("world!$", "Hello, world!"))  # $: 문자열이 맨 뒤에 오는지 판단

## 지정된 문자열이 하나라도 포함되는지 판단
print(re.match("hello|world", "hello"))  # hello 또는 world가 있는지 판단

