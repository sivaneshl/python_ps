t = ('Norway', 4.953, 4)    # similar to list, but use ( )

print(t[1])     # access the elements of a tuple using []

print(len(t))   # length of a tuple

for item in t:  # items in a tuple can be accessed using a for
    print(item)

print(t + (747, 'Bench'))   # can be concatenated using + operator
print(t)    # immutable

print(t * 3)    # can be used with multiply operator

# nested tuples
a = ((120, 567), (747, 950), (474, 748), (747,738))     # nested tuples
print(a[3])
print(a[3][1])

# single element tuple
h = (849)
print(h,  type(h))  # this is treated as a int as a math exp

h = (858,)  # single element tuple with trailing comma
print(h, type(h))

e = ()      # empty tuple
print(e, type(e))

# parenthesis of literal tuples may be omitted
p = 1, 1, 3, 5, 6, 9
print(p, type(p))



