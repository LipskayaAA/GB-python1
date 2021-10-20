def third_func(a,b,c):
    try:
        num1 = int(a)
        num2 = int(b)
        num3 = int(c)
    except (ValueError):
        print("Неверный формат")
    else:
        set = [a,b,c]
        print(f"сумма: {sum(set) - min(set)}")
third_func(35,'sdf',465)