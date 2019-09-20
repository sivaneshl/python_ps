from math import factorial
s = {factorial(x) for x in range(20)}
print(s)
print(type(s))