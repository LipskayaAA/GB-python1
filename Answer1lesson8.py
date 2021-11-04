class Data:
    def __init__(self,day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def num(cls,day_month_year):
        number = day_month_year.split('-')
        try:
            return f'{int(number[0])}, {int(number[1])}, {int(number[2])}'
        except:
            return f'Uncorrect'

    @staticmethod
    def val(day,month,year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Correct'
                else:
                    return f'Uncorrect year'
            else:
                return f'Uncorrect month'
        else:
            return f'Uncorrect day'

    def __str__(self):
        return f'Текущая дата {Data.num(self.day_month_year)}'
today = Data('11-1-2001')
print(Data.num('11-1-2001'))

