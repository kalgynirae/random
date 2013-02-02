import itertools
from math import sqrt

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

def sieve_of_eratosthenes(limit):
    """Return the prime numbers less than limit

    >>> sieve_of_eratosthenes(7)
    [2, 3, 5]

    """
    # Start with a list of all integers up to max
    l = list(range(limit))
    l[1] = 0 # 1 is not prime
    stop = sqrt(limit)
    for n in l:
        if n != 0:
            m = n * n
            while m < limit:
                l[m] = 0
                m += n
    return [x for x in l if x != 0]

def primes(max=None):
    """Generate prime numbers

    Stolen from
    http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/

    >>> list(primes(5))
    [2, 3, 5]

    """
    yield 2
    D = {}
    for q in itertools.count(3, 2):
        if max and q > max:
            raise StopIteration
        p = D.pop(q, None)
        if p is None:
            # q is prime
            yield q
            D[q * q] = 2 * q
        else:
            # q is composite
            x = p + q
            while x in D:
                x += p
            D[x] = p

def factors(x):
    """Return all factors of n"""
    factors = set()
    for n in range(1, int(sqrt(x)) + 1):
        if x % n == 0:
            factors.add(n)
            factors.add(x // n)
    return factors

def prime_factors(n):
    prime_generator = primes()
    while n > 1:
        p = next(prime_generator)
        while n % p == 0:
            n = n // p
            yield p

if __name__ == '__main__':
    import doctest
    doctest.testmod()
