from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("выработка в часах: ", first_param)
print("ставка в час: ", second_param)
print("премия: ", third_param)
def func_1 ():
    try:
        a = int(first_param)
        b = int(second_param)
        c = int(third_param)
    except ValueError:
        print('Введите числовые значения')
    else:
        return ((a + b) / c)
print(f"заработная плата: {round(func_1(),2)}")
