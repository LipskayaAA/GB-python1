#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#print(f'''IP address: {oct1}:{oct2}:{oct3}:{oct4}''')
time = int(input("Please, record the time per seconds: "))
hour = time // 3600
minute = (time - (hour*3600)) // 60
secon = time - (minute*60) - (hour*3600)
if (hour < 10) and (minute < 10) and (secon < 10):
    print(f"{0}{hour}:{0}{minute}:{0}{secon}")
elif (hour < 10) and (minute < 10):
    print(f"{0}{hour}:{0}{minute}:{secon}")
elif (hour < 10) and (secon < 10):
    print(f"{0}{hour}:{minute}:{0}{secon}")
elif (minute < 10) and (secon < 10):
    print(f"{hour}:{0}{minute}:{0}{secon}")
elif (hour < 10):
    print(f"{0}{hour}:{minute}:{secon}")
elif (minute < 10):
    print(f"{hour}:{0}{minute}:{secon}")
elif (secon < 10):
    print(f"{hour}:{minute}:{0}{secon}")
else:
    print(f"{hour}:{minute}:{secon}")
