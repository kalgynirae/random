import inspect
from numbers import Number

class FunctionBuilder:
    """umm...

    Examples:
    >>> x = FunctionBuilder('x')
    >>> f = (x + 5) * (x - 3)
    >>> f(x=0)
    -15
    >>> f(x=3)
    0
    >>> f(x=4)
    9
    >>> f(x=5)
    20

    >>> f = x**2 - 4 * x + 4
    >>> f(x=0)
    4
    >>> f(x=2)
    0
    >>> f(x=6)
    16

    >>> f = 5 - (x % 8 + 17 // x)
    >>> f(x=4)
    -3

    >>> x = FunctionBuilder('x')
    >>> y = FunctionBuilder('y')
    >>> f = 4*x - y**2 + y//7
    >>> f(x=2, y=8)
    -55

    """
    __slots__ = ('_operations', 'name')

    def __init__(self, name):
        self._operations = []
        self.name = name

    def __copy__(self):
        f = FunctionBuilder(self.name)
        f._operations = self._operations[:]
        return f

    def __call__(self, **kwargs):
        result = kwargs[self.name]
        for op, other in self._operations:
            if isinstance(other, FunctionBuilder):
                other = other(**kwargs)
            result = op(result, other)
        return result

    def _(func):
        def fred_johnson(self, other):
            f = self.__copy__()
            f._operations.append((func, other))
            return f
        return fred_johnson

    __add__ = _(lambda x, y: x + y)
    __radd__ = _(lambda x, y: y + x)
    __sub__ = _(lambda x, y: x - y)
    __rsub__ = _(lambda x, y: y - x)
    __mul__ = _(lambda x, y: x * y)
    __rmul__ = _(lambda x, y: y * x)
    __truediv__ = _(lambda x, y: x / y)
    __rtruediv__ = _(lambda x, y: y / x)
    __floordiv__ = _(lambda x, y: x // y)
    __rfloordiv__ = _(lambda x, y: y // x)
    __mod__ = _(lambda x, y: x % y)
    __rmod__ = _(lambda x, y: y % x)
    __pow__ = _(lambda x, y: x ** y)
    __rpow__ = _(lambda x, y: y ** x)

def vars(names):
    return [FunctionBuilder(name) for name in names]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
