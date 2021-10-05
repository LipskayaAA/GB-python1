#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#print(f'''IP address: {oct1}:{oct2}:{oct3}:{oct4}''')
time = int(input("Please, record the time per seconds: "))
hour = time // 3600
minute = (time - (hour*3600)) // 60
secon = time - (minute*60) - (hour*3600)
print(f"{hour}:{minute}:{secon}")
