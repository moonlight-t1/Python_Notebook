import turtle as t

n, line = map(int, input().split())
t.shape("turtle")
# t.speed("fastest")

for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)
