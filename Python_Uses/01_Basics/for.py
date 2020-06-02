# 반복문 for

"""enumerate"""
student = [{"박은빈": 100}, {"이세영": 200}, {"송지원": 300}]

for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{}. 이름: {} 점수: {}".format(s, name, value))

"""컴프리헨션"""
result = []
for num in range(1, 6):
    result.append(num + 5)

result = [num + 5 for num in range(1, 6)] # 컴프리헨션
print(result)

result = [num + 5 for num in range(1, 10) if num % 2 == 0] # 짝수만 num에 들어간다
print(result)

# 다음과 같이 풀어 쓸 수 있다
for num in range(1, 10):
    if num % 2 == 0:
        result.append(num * 3)
print(result)

# 구구단 출력
gugudan = ["{} x {} = {}".format(i, j, i * j) for i in range(2, 10) for j in range(1, 10)]
print(gugudan)