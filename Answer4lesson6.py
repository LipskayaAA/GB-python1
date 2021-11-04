from random import choice
class Car:
    dir = ['south', 'west','east','north']
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{name}\n{color}\n{is_police}')
    def go(self):
        print(f"{self.name} - машина поехала")
    def stop(self):
        print(f"{self.name} - машина остановилась")
    def turn(self):
        print(f"{choice(self.dir)} - направление")
    def show_speed(self):
        print(f"{self.speed} - скорость")
class TownCar(Car):
    def show_speed(self):
        return f"{self.name}, {self.speed} - Превышение" if self.speed>60 else super().show_speed()
class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}, {self.speed} - Превышение" if self.speed>40 else super().show_speed()
class SportCar(Car):
    """adad"""


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed,color,name,is_police=True)
pol = PoliceCar(80, 'white', 'dd')
town = TownCar(75, 'green', 'qq')
work = WorkCar(45, 'black', 'tt')
sport = SportCar(120, 'white', 'yy')
cars_list = [pol,town,work,sport]
for i in cars_list:
    i.go()
    i.turn()
    print(i.show_speed())
    i.stop()