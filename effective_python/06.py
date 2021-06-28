## unpacking
item = {"apple", "banana"}
first, second = item
print(first, "&", second)

## bubble_sort
def bubble_sort(a):
    for _ in range(len(a)):  # list 길이만큼
        for i in range(1, len(a)):  # 1부터 list 길이 만큼
            if a[i] < a[i - 1]:  # 오름 차순 정렬
                a[i - 1], a[i] = a[i], a[i - 1]


names = ["프레즐", "당근", "쑥갓", "베이컨"]
bubble_sort(names)
print(names)

## list unpacking
snacks = [("베이컨", 350), ("도넛", 240), ("머핀", 190)]

for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} - {calories}")

