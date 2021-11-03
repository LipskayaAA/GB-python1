class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
my_list = []

while True:
    try:
        inp_data = input("Введите  число, если хотите выйти введите 'exit': ")
        if not inp_data.isnumeric():
            raise OwnError("Вы ввели не число")
        else:
            inp_data = int(inp_data)
            my_list.append(inp_data)
    except OwnError as err:
        print(err)
    else:
        print(f"Все хорошо. Ваше число: {my_list}")
    if inp_data == 'exit':
        print(f"Ваше число: {my_list}")
        break


