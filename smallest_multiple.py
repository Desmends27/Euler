from math import gcd
from functools import reduce
#smalles multiple of a number is the same as the lcm

def lcm(a, b)-> int:
    '''
    Returns the lcm of a and b
    using the formula a*b/gcd(a,b)
    '''
    return  (a*b) // gcd(a, b)

def smallest_multiple(number) -> int:
    '''
    Returns the smallest multiple using the lcm method and applying
    reduce on each of the numbers
    '''
    return reduce(lcm, range(1, number+1))

num = smallest_multiple(20)
print(num)