"""Usage: python crypto_solver.py GOAL NUMBER...
Find an expression using the four basic operations and each NUMBER once
that evaluates to GOAL.
"""

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

def solve(goal, numbers, *, print_solutions=False):
    solutions = []
    number_sets = permutations(numbers)
    seen_number_sets = set()
    for ns in number_sets:
        if ns not in seen_number_sets:
            seen_number_sets.add(ns)
            operator_sets = product(operators, repeat=len(numbers)-1)
            for os in operator_sets:
                tree_set = trees(len(numbers) - 1)
                for tree in tree_set:
                    try:
                        result = evaluate(tree, list(os), list(ns))
                    except ZeroDivisionError:
                        pass
                    else:
                        if result == goal:
                            e = evaluate(tree, list(os), list(ns),
                                         return_expression=True)
                            solutions.append(e)
                            if print_solutions:
                                print(e)
    return solutions

if __name__ == '__main__':
    try:
        goal = int(sys.argv[1])
        numbers = [int(sys.argv[n]) for n in range(2,len(sys.argv))]
        if not numbers:
            raise IndexError
    except (ValueError, IndexError):
        print(__doc__, file=sys.stderr, end='')
    else:
        solve(goal, numbers, print_solutions=True)
