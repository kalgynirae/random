def flatten(s):
    for item in s:
        try:
            yield from flatten(item)
        except TypeError:
            yield item
