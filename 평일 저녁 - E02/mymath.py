
def mymultiply(x, y, *args):
    result = x * y
    for i in args:
        result *= i
    return result
