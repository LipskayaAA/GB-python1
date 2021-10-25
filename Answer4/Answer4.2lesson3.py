def fourth_func():
    a = input('Введите действительно положительное число: ')
    b = input("Введите отрицательное целое число: ")
    try:
        num1 = float(a)
        num2 = int(b)
    except ValueError:
        print("Неправильно заданы данные")
    else:
        for num1 in range(1,abs(num2)):
            num1 = num1*num1
        return (1 / num1)
f = fourth_func()
print(f)