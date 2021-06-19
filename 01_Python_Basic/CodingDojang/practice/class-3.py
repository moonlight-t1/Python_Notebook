class A:
    def greeting(self):
        print("Hello, A")


class B(A):
    def greeting(self):
        print("Hello, B")


class C(A):
    def greeting(self):
        print("Hello, C")


class D(B, C):  # 다중 상속
    pass


x = D()
x.greeting()

print(D.mro())
