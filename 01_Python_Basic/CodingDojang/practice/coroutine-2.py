## 문자열 검색 코루틴 만들기
def find(word):
    result = False
    while True:
        line = yield result
        result = word in line


f = find("Python")
next(f)

print(f.send("Hello, Python!"))
print(f.send("Hello, world!"))
print(f.send("Python Script!"))

f.close()
