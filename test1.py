# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
profession = input("Enter yor profession: ")
message = (f"Hello {name}! \n"
    f"Your profession is {profession} and your age is {age}.")
print(message)
