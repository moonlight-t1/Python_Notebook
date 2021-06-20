## 시간 이터레이터 만들기
class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop - self.start:
            time = self.start + index
            hour = time // 3600 % 24
            minute = time // 60 % 60
            second = time % 60
            return f"{hour:02}:{minute:02}:{second:02}"
        else:
            raise IndexError


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print("\n", TimeIterator(start, stop)[index], sep="")

