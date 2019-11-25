class Bicycle():
    def __init__(self, wheel_size=10, color='white'):
        self.__wheel_size = wheel_size  # Python에서의 private 방식 : 언더바(_) 2개를 변수명 앞에 붙인다.
        self.__color = color
        self.tmp = 100  # 언더바 1개는 private 불가능

    def move(self, speed):
        pass

    def turn(self, direction):
        pass

    def stop(self):
        print("자전거({} {}): 정지".format(self.__wheel_size, self.__color))

    # def __str__(self) -> str:       # object.__str__() overriding
    #     return str("자전거({}, {})".format(self.wheel_size, self.color))


class Car(Bicycle):
    def stop(self):
        print("자동차({} {}): 정지".format(self.wheel_size, self.color))


if __name__ == "__main__":
    my_bicycle = Bicycle()
    my_bicycle2 = Bicycle(26, 'red')
    # my_bicycle.wheel_size = 26
    # my_bicycle.color = "red"
    my_bicycle.stop()
    my_bicycle2.stop()

    print(my_bicycle)
    print(my_bicycle2)
    print(my_bicycle2.tmp)
