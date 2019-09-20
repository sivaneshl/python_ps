# sets

p = {1, 2, 3, 5, 8, 13}  # should be unique elements - duplicates are discarded
print(p, type(p))

s = set()       # empty set
print(s)

# convert list to set
t = [1, 4, 2, 1, 7, 9, 9]
s = set(t)      # duplicates are removed
print(s)

# itreable
for x in s:
    print(x)

# membership
print(3 in s)
print(3 not in s)

# add elements to a set using add method
s.add(12)
print(s)

# add multiple elements to a set using update method
s.update([15, 17, 19])
print(s)

# remove items from the set
s.remove(17)
print(s)
s.discard(17)
print(s)

# copy
m = s.copy()
print(m)

k = set(m)
print(k)



