year, month, day, hour, minute, sec = map(int, input().split())

print(year, month, day, sep="-", end="T")
print(hour, minute, sec, sep=":")

