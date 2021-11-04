import json
with open('new_f.txt','w', encoding ='utf-8') as new:
    with open('new_f1.txt','w', encoding ='utf-8') as new1:
        v = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in new1}
        r = [v,{'Средняя прибыль': sum([int(i) for i in v.values() if int(i)>0]) / len([int(i) for i in v.values() if int(i)>0])}]
    json.dump(r, new, ensure_ascii=False, indent=4)



