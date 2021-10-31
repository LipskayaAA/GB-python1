class Cell:
    def __init__(self, a):
        self.a = a
    def  make_order(self, b):
        self.b = b
        return '\n'.join('*' * b for _ in range(self.a // b)) + '\n'.join('*'*(self.a % b))
    def __str__(self):
        return Cell(f"{self.a}")
    def __add__(self, other):
        return Cell(f'Sum is {self.a + other.a}')
    def __sub__(self, other):
        if self.a - other.a > 0:
            return Cell(f'Sub is {self.a - other.a}')
        else:
            return  Cell(f'Error')
    def __mul__(self, other):
        return Cell(f'Mul is {self.a * other.a}')
    def __truediv__(self, other):
        return Cell(f'Div is {self.a // other.a}')
