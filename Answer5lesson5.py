with open('new_f3.txt','w', encoding ='utf-8') as new:
    a = input('введите данные через пробел: ')
    print(sum(float(x) for x in a.split()))


