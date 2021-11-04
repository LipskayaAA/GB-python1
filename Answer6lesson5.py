with open('new_f.txt','r', encoding ='utf-8') as new:
    dic = {}
    a = new.readlines()
    for line in a:
        try:
            c = ''.join(i if i in '1234567890' else ' ' for i in line)
            b = [int(i) for i in c.split()]
            dic[line.split()[0]] = sum(b)
        except ValueError:
            pass
    print(dic)