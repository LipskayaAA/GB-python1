# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
stroka = input("please, enter:")
my_list3 = stroka.split()
for i, v in enumerate(my_list3, 1):
        print(str(i) + ' строка ' + str(v[0:10]))
