## for ~ else
for i in range(3):
    print("Loop", i)
else:  # 루프가 끝까지 완전히 돌면 else 실행
    print("Else block!")


for i in range(3):
    print("Loop", i)
    if i == 1:
        break
else:  # 실행이 안된다
    print("Else block!")

## 서로소
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime


assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)
assert coprime_alternate(3, 6)  # assert error

