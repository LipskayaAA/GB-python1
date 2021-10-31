from itertools import count
i = 0
for i in count(3):
    if i>10:
        break
    else:
        print(i)
        i+=1
my_list = [300, 2, 12, 44, 1, 1]
from itertools import cycle
с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1
