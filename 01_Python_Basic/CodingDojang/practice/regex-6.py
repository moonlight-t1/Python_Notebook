## 이메일 주소 검사하기
import re

p = re.compile("^http[s]*://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]+")


def match(url):
    if p.match(url):
        return True
    else:
        return False


url = input()
print(match(url))

