# 유니코드와 인코딩

# utf-8
# 1110xxxx 10xxxxxx 10xxxxxx 형식으로 인코딩된다.

a = '가'  # 1010110000000000
print(a)
print(ord(a))  # 유니코드 10진수 값
print(hex(ord(a)))  # 16진수
print(bin(ord(a)))  # 2진수
print("\n")

print(hex(0b11101010))
print(hex(0b10110000))
print(hex(0b10000000))
print("\n")

# 텍스트 파일을 읽어올 때 적절한 코덱으로 디코딩해줘야 한다
file = open("utf8.txt", mode="rb")
print(file.read().decode("utf-8"))
file.close()
