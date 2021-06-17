import turtle as t

## 사각형 그리기
t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.right(90)


## 다각형에 색칠하기
n = 6
t.shape("turtle")
t.color("red")
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.end_fill()

## 복잡한 그림
t.shape("turtle")
t.speed("fastest")  # 거북이 속도를 가장 빠르게 설정
for i in range(300):  # 300번 반복
    t.forward(i)  # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)  # 오른쪽으로 91도 회전


t.mainloop()
