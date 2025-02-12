class AdvancedTuple(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, args)

    def __add__(self, other):
        if isinstance(other, tuple):
            # self.__class__ = tuple
            # return AdvancedTuple(*(self + other))]
            _a_tuple = super(tuple, self)
            # print(_a_tuple)
            return AdvancedTuple(*(_a_tuple.__add__(other)))
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, tuple):
            return AdvancedTuple(*(item for item in self if item not in other))
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, n):
        if isinstance(n, int):
            return AdvancedTuple(*(self * n))
        else:
            raise TypeError("Unsupported operand type for *")

    def __getitem__(self, index):
        if isinstance(index, int):
            return super().__getitem__(index)
        elif isinstance(index, slice):
            return AdvancedTuple(*super().__getitem__(index))
        else:
            raise TypeError("Unsupported index type")

    def __contains__(self, item):
        return item in self

    def count(self, item):
        return super().count(item)

    def index(self, item, start=0, stop=None):
        return super().index(item, start, stop)
def main():
    # Your main code here
    my_tuple = AdvancedTuple(1,2,3)
    a_tuple = (4,5,6)
    # print(my_tuple.__add__(a_tuple))
    print(my_tuple+a_tuple)
    # pass

if __name__ == "__main__":
    main()
