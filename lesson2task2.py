#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = input()
my_list1 = []
i = 0
my_list3 = my_list.split()
b = len(my_list3)
if b % 2 == 0:
    for i in range(0, len(my_list3), 2):
        var_1, var_2 = my_list3[i], my_list3[i+1]
        var_1, var_2 = var_2, var_1
        my_list1.append(var_1)
        my_list1.append(var_2)
    print(my_list1)
else:
    for i in range(0, len(my_list3) - 1, 2):
        var_1, var_2 = my_list3[i], my_list3[i+1]
        var_1, var_2 = var_2, var_1
        my_list1.append(var_1)
        my_list1.append(var_2)
    my_list1.append(my_list3[b - 1])
    print(my_list1)
