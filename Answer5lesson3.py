def fifth_func():
    i = 0
    while True:
        my_list = input('введите последовательность, если выйти нажмите "e":').split()
        for v in my_list:
            if v.lower() == "e":
                return i
            else:
                i = i + int(v)
        my_list2 = [int(x) for x in my_list]
        print(f"{sum(my_list2)},({i})")
print(fifth_func())





