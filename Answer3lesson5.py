with open('new_f.txt','r', encoding ='utf-8') as new:
    a = 0
    for num, line in enumerate(new, 1):
        try:
            a = a+(float(line.split()[1]))
            if float(line.split()[1]) > 20000:
                print(line.split()[0])
        except ValueError:
            pass
    print(f'{a/num} - средний доход')

