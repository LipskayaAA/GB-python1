def generator(b):
    x = 1
    for el in range(b+1):
        yield f"{el}!={x}"
        x = x *(el+1)

for el in generator(int(input())):
    print(el)