class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        print(f"Имя - {self.name} \nФамилия - {self.surname} \nДолжность - {self.position}")
    def get_total_income(self):
        print(f"Доход - {sum(self._income.values())}")
a = Position("Ivan", "Ivanov", "sss", 5000, 2000)
a.get_full_name()
a.get_total_income()