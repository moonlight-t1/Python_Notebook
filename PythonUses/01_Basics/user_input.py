"""사용자 입력 받기"""

langs = ["한국어", "English"]

for i, l in enumerate(langs, start=1):
    print("{}. {}".format(i, l))

while True:
    sel = input("언어를 선택하세요. : ")

    if not sel.isnumeric():
        continue

    sel = int(sel)
    if 0 < sel < 3:
        break

print("사용자가 선택한 언어는 {} 입니다.".format(langs[sel-1]))


"""입력한 숫자가 소수인지 판단"""
while True:
    num = input("2 이상의 숫자를 입력하세요 > ")
    if not num.isnumeric():
        continue
    num = int(num)
    if num < 2:
        continue
    break

# Method 1
isPrime = True  # 소수라 가정하고 시작
for n in range(2, num):  # 2부터 num까지 나눠본다
    if num % n == 0:
        isPrime = False
        break

if isPrime:
    print("소수 입니다")
else:
    print("소수가 아닙니다")

# Method 2 : 에레토스테네스의 체
prime_list = [False, False] + [True] * (num - 1)  # 0, 1을 제외한 나머지 수는 소수라 가정
prime = []  # 최종 소수 저장

for i in range(2, num + 1):
    if prime_list[i]:
        for j in range(2 * i, num + 1, i):  # 2*i부터 num+i만큼 i배수들을 모두 false
            prime_list[j] = False

primes = [i for i in range(2, num + 1) if prime_list[i]
          == True]  # Array에서 True인 것만 출력
print(primes)

if isPrime:
    print("소수 입니다")
else:
    print("소수가 아닙니다")
