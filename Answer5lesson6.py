class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title
    def draw(self):
        print(self.title)
class Pen(Stationery):
    def draw(self):
        print(f'зарисовка с помощью - {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'зарисовка с помощью - {self.title}')
class Marker(Stationery):
    def draw(self):
        print(f'зарисовка с помощью - {self.title}')
a = Stationery()
pen = Pen('pen')
pencil = Pencil('pencil')
marker = Marker('marker')
list = [a,pen,pencil,marker]
for i in list:
    i.draw()



