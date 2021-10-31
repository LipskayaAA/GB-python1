from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod

    def cons(self):
        pass

    def __add__(self, other):
       return self.cons + other.cons


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if size > 0:
            self.__size = size

    @property
    def cons(self):
        return self.__size / 6.5 + 0.5
class Costume(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 0:
            self.__size = size

    @property
    def cons(self):
        return self.__size*2 + 0.3
a = Coat(42)
b = Costume(158)
print(a+b)

