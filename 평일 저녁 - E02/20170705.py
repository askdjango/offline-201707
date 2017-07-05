import mymath
from mymath import mymultiply

def mysum(x, y, *args):
    result = x + y
    for i in args:
        result += i
    return result

# def mymultiply(x, y):
#     return x + Y

print(mysum(1, 2, 3, 4, 5))
print(mysum(1, 2, 3, 4, 5, 6))
print(mysum(1, 2, 3, 4, 5, 6, 7))
print(mymath.mymultiply(1, 2, 3, 4, 5))

print(mymultiply(1, 2, 3, 4, 5, 6, 7))
