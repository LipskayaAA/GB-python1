with open('new_f.txt','r', encoding ='utf-8') as new:
    a = [f'{num} строка, {len(line.replace(" ",""))}-элементов'  for num, line in enumerate(new, 1)]
    print(a)
    count = sum(1 for line in a if line.rstrip('\n'))
    print(f'Всего строк - {count}')