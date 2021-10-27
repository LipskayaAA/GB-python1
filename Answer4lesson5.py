r = {'One':'Один', 'Two':'Два', 'Three':'Три','Four':'Четыре'}
with open('new_f.txt','w', encoding ='utf-8') as new:
    with open('new_f1.txt', encoding='utf-8') as new1:
        new.writelines([line.replace(line.split()[0], r.get(line.split()[0])) for line in new1])

