def in_func():
    my_list = input('введите текст: ')
    my_list2 = " ".join(my_list.split())
    print(my_list2.title())
print(in_func())