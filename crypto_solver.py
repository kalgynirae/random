from itertools import permutations, product
from operator import add, mul, sub, truediv
import sys

operators = [add, mul, sub, truediv]
operator_symbols = dict(zip(operators, list('+*-/')))

def trees(nodes):
    if nodes == 0:
        yield None
    else:
        for n in range(nodes):
            for p in product(trees(nodes - 1 - n), trees(n)):
                yield tuple('o') + p

def evaluate(tree, operators, values, return_expression=False):
    if isinstance(tree, tuple):
        op = operators.pop()
        left = evaluate(tree[1], operators, values, return_expression)
        right = evaluate(tree[2], operators, values, return_expression)
        if return_expression:
            return "({} {} {})".format(left, operator_symbols[op], right)
        else:
            return op(left, right)
    else:
        return values.pop()

goal = int(sys.argv[1])
numbers = [int(sys.argv[n]) for n in range(2,7)]

number_sets = permutations(numbers)
for ns in number_sets:
    operator_sets = product(operators, repeat=len(operators))
    for os in operator_sets:
        tree_set = trees(4)
        for tree in tree_set:
            try:
                result = evaluate(tree, list(os), list(ns))
            except ZeroDivisionError:
                pass
            else:
                if result == goal:
                    print(evaluate(tree, list(os), list(ns), True))
