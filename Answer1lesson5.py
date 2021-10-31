with open('new_f.txt','w', encoding ='utf-8') as new:
    while True:
        a = input('введите данные, если хотите закончить введите пустую строку: ')
        print(a, file=new)
        if not a:
            break