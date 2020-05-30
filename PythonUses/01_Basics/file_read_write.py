""" 파이썬에서 파일 읽고 쓰기"""
# file = open("sample.txt", mode="w", encoding="utf-8")
# file.write("안녕 파이썬")
# file.close()

# rfile = open("sample.txt", mode="r", encoding="utf-8")
# content = rfile.read() # 전체 읽기
# content2 = rfile.readline() # 한줄 읽기
# print(content2)

# for l in rfile:
#     print(l)

""" 포인터로 읽기"""
# print(rfile.tell())  # 현재 포인터 위치
# a = rfile.read(10)  # 10글자 읽기
# print(rfile.tell())
# print(a)
# rfile.seek(0)  # 처음으로 이동
# print(a)
# rfile.close()

"""with"""
# with open("sample.txt", mode="r", encoding="utf-8") as file:
#     print(file.read)

with open("sample.txt", mode="r", encoding="utf-8") as s, \
        open("sample2.txt", mode="w", encoding="utf-8") as t:
    t.write(s.read().replace("파이썬", "Python"))
