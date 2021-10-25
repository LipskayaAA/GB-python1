#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
a = int(input("Введите номер месяца: "))
my_dict = {1: "Winter", 3: "Spring", 2:"Winter", 4: "Spring", 5: "Spring", 6: "Summer", 8: "Summer", 7:"Summer", 9:"Autumn", 10:"Autumn",11:"Autumn",12:"Winter"}
print(my_dict.get(a))