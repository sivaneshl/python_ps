from pprint import pprint as pp
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# print(is_prime(3))


pp({x: is_prime(x) for x in range(21)})

# filter only is_prime = True
pp([x for x in range(20) if is_prime(x)])
