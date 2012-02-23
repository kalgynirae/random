class FunctionBuilder:
    """umm...

    Examples:
    >>> x = FunctionBuilder()
    >>> f = (x + 5) * (x - 3)
    >>> f
    ((x + 5) * (x - 3))
    >>> f(0)
    -15
    >>> f(3)
    0
    >>> f(4)
    9
    >>> f(5)
    20

    >>> f = x**2 - 4 * x + 4
    >>> f
    (((x ** 2) - (4 * x)) + 4)
    >>> f(0)
    4
    >>> f(2)
    0
    >>> f(6)
    16

    >>> f = 5 - (x % 8 + 17 // x)
    >>> f
    (5 - ((x % 8) + (17 // x)))
    >>> f(4)
    -3

    """
    __slots__ = ('_operations', 'name')

    def __init__(self, name="x"):
        self._operations = []
        self.name = name

    def __copy__(self):
        f = FunctionBuilder()
        f._operations = self._operations[:]
        return f

    def __repr__(self):
        s = self.name
        for op, other in self._operations:
            if op[-1] == 'r':
                s = '({} {} {})'.format(other, op[:-1], s)
            else:
                s = '({} {} {})'.format(s, op, other)
        return s

    def __call__(self, x):
        result = x
        for op, other in self._operations:
            if isinstance(other, FunctionBuilder):
                other = other(x)
            if op == '+':
                result = result + other
            elif op == '+r':
                result = other + result
            elif op == '-':
                result = result - other
            elif op == '-r':
                result = other - result
            elif op == '*':
                result = result * other
            elif op == '*r':
                result = other * result
            elif op == '/':
                result = result / other
            elif op == '/r':
                result = other / result
            elif op == '//':
                result = result // other
            elif op == '//r':
                result = other // result
            elif op == '%':
                result = result % other
            elif op == '%r':
                result = other % result
            elif op == '**':
                result = result ** other
            elif op == '**r':
                result = other ** result
            else:
                raise ValueError("Invalid operation: {}".format(op))
        return result

    def __add__(self, other):
        f = self.__copy__()
        f._operations.append(('+', other))
        return f

    def __radd__(self, other):
        f = self.__copy__()
        f._operations.append(('+r', other))
        return f

    def __sub__(self, other):
        f = self.__copy__()
        f._operations.append(('-', other))
        return f

    def __rsub__(self, other):
        f = self.__copy__()
        f._operations.append(('-r', other))
        return f

    def __mul__(self, other):
        f = self.__copy__()
        f._operations.append(('*', other))
        return f

    def __rmul__(self, other):
        f = self.__copy__()
        f._operations.append(('*r', other))
        return f

    def __truediv__(self, other):
        f = self.__copy__()
        f._operations.append(('/', other))
        return f

    def __rtruediv__(self, other):
        f = self.__copy__()
        f._operations.append(('/r', other))
        return f

    def __floordiv__(self, other):
        f = self.__copy__()
        f._operations.append(('//', other))
        return f

    def __rfloordiv__(self, other):
        f = self.__copy__()
        f._operations.append(('//r', other))
        return f

    def __mod__(self, other):
        f = self.__copy__()
        f._operations.append(('%', other))
        return f

    def __rmod__(self, other):
        f = self.__copy__()
        f._operations.append(('%r', other))
        return f

    def __pow__(self, other):
        f = self.__copy__()
        f._operations.append(('**', other))
        return f

    def __rpow__(self, other):
        f = self.__copy__()
        f._operations.append(('**r', other))
        return f

if __name__ == '__main__':
    import doctest
    doctest.testmod()
