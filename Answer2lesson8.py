class ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите делимое: ")
inp_data1 = input("Введите делитель: ")

try:
    inp_data = float(inp_data)
    inp_data1 = float(inp_data1)
    inp_data3 = inp_data / inp_data1
    if inp_data1 == 0:
        raise ZeroDivisionError("Вы ввели ноль!")
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data3}")