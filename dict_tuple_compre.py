from pprint import pprint as pp
from filter_compr import is_prime

divisors = {x*x: (1, x, x*x) for x in range(10) if is_prime(x)}
pp(divisors)