from itertools import chain, repeat

def in_words(number):
    """Return the word form of numbers up to 9999"""
    names = (" one two three four five six seven eight nine ten eleven twelve "
             "thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
             "".split(' '))
    tens_names = ("  twenty thirty forty fifty sixty seventy eighty ninety"
                  "".split(' '))
    thousands, hundreds, tens, ones = (int(d) for d in '{:04}'.format(number))
    words = []
    yes_and = False
    if thousands > 0:
        words.extend([names[thousands], 'thousand'])
        yes_and = True
    if hundreds > 0:
        words.extend([names[hundreds], 'hundred'])
        yes_and = True
    if yes_and and (ones != 0 or tens != 0):
        words.append('and')
    if tens == 1:
        words.append(names[tens * 10 + ones])
    else:
        words.extend([tens_names[tens], names[ones]])
    return ' '.join(words)
