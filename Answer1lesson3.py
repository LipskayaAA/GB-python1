def first_func(a,b):
    try:
        num1 = int(a)
        num2 = int(b)
        num3 = num1 / num2
    except (ValueError,ZeroDivisionError):
        print("Неверный формат, либо происходит делние на ноль")
    else:
        print(f"Значение деления: {a / b}")
first_func(2, 3)
