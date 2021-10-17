def fourth_func():
    a = input('Введите действительно положительное число: ')
    b = input("Введите отрицательное целое число: ")
    try:
        num1 = float(a)
        num2 = int(b)
    except ValueError:
        print("Неправильно заданы данные")
    else:
        x = num1 ** num2
        return x
f = fourth_func()
print(f)