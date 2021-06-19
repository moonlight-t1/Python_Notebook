## 세트 만들기
fruits = {"strawberry", "grape", "orange", "pineapple", "cherry", "strawberry", "grape"}
print(fruits)

for i in fruits:
    print(i)

## 세트에 특정 값이 있는지 확인
print("orange" in fruits)
print("peach" in fruits)

## set를 이용하여 세트 만들기
a = set("apple")
print(a)

c = {}  # 이건 빈 세트가 아닌 빈 딕셔너리다

## frozenset
a = frozenset(range(10))  # 내용을 변경할 수 없다
print(a)

# frozenset은 중첩이 가능하다
b = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(b)
