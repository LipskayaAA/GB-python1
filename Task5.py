#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
r = int(input("Значение выручки: "))
c = int(input("Значение издержек: "))
if r > c:
    print('Прибыль составила - ',"%.2f" % (((r - c) / c) * 100), '%' )
    d = int(input("Введите количество сотрудников: "))
    print('Прибыль на сотрудника - '"%.2f" % ((r - c) / d))
elif r == c:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

