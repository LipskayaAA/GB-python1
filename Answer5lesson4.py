from functools import reduce
new_list = [i for i in range(99,1001) if i%2 ==0]
def func_1(a,v):
    return a*v
print(reduce(func_1,(new_list)))
print(new_list)