from itertools import chain, cycle, islice
from string import ascii_lowercase as AL, ascii_uppercase as AU

test_string = """Hi there!

I'm writing you this message from the bottom of an endless pit!
(The endlessness is in the upward direction, obviously.)

Yup.
Bye!"""

def rot13(s):
    d = dict(chain(*map(lambda x: zip(x, islice(cycle(x), 13, None)), (AL, AU))))
    return ''.join(map(lambda c: d[c] if c in d else c, s))
