my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list.remove(i) for i in my_list if my_list.count(i) > 1]
print(f"Исходный список: {my_list}")
