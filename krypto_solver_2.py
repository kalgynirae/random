"""Usage: python krypto_solver_2.py GOAL NUMBER...
Find an expression using the four basic operations and each NUMBER once
that evaluates to GOAL.
"""
import sys

operators = (lambda a, b: (a[0] + b[0], "({} + {})".format(a[1], b[1])),
             lambda a, b: (a[0] * b[0], "({} * {})".format(a[1], b[1])),
             lambda a, b: (a[0] - b[0], "({} - {})".format(a[1], b[1])),
             lambda b, a: (a[0] - b[0], "({} - {})".format(a[1], b[1])),
             lambda a, b: (a[0] / b[0] if b[0] != 0 else float('inf'),
                           "({} / {})".format(a[1], b[1])),
             lambda b, a: (a[0] / b[0] if b[0] != 0 else float('inf'),
                           "({} / {})".format(a[1], b[1])))

def one_at_a_time(s):
    for i in range(len(s)):
        yield s[i], s[:i] + s[i+1:]

def results(numbers):
    if len(numbers) == 2:
        for operator in operators:
            yield operator(numbers[0], numbers[1])
    else:
        for number, others in one_at_a_time(numbers):
            for others_result in results(others):
                for operator in operators:
                    yield operator(number, others_result)

def solve(goal, numbers, print_solutions=True):
    solutions = []
    for result, expression in results([(n, str(n)) for n in numbers]):
        if result == goal:
            solutions.append(expression)
            if print_solutions:
                print(expression)
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
