class CarMixIn:
    def ready(self):
        print("믹스인 레디")

    def start(self):
        print("{}가 {} 속도로 달립니다.".format(self.name, self.speed))


class Performance():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.ready()


# 믹스인
# 다중 상속을 받아서 SuperCar를 만들었다.
# 두 클래스의 모든 기능을 사용할 수 있다.
# 믹스인 하면서 다른 클래스에 있는 함수를 사요할 수 있게 된다.
class SuperCar(CarMixIn, Performance):
    def show_info(self):
        print("{}는 {} 속도의 성능입니다.".format(self.name, self.speed))

    def start(self):  # 오버라이딩(자식 것의 호출)
        super().start()  # super() => 부모 클래스의 생성자 호출하게 해준다.
        print("스타트")


s = SuperCar("람보르", 300)
s.show_info()
s.start()
