# dictionary

d = {"Alice": 32, "Bob": 28, "Charlie": 31, "Daniel": 24}
print(d)
print(d["Bob"])     # can be accessed using keys only

names_and_ages = [("Alice", 32), ("Bob", 28), ("Charlie", 31), ("Daniel", 24)]
d = dict(names_and_ages)    # dict() constructor accepts iterable series of key-value 2-tuples
print(d)

# dict() constructor accepts key value pairs
new_dict = dict(a="alpha", b='bravo', c='charlie', d='delta', e='echo')
print(new_dict)

# dict() constructor accepts another dict
dict1 = dict(new_dict)
print(dict1)


# copy dict using copy method
new_dict = d.copy()
print(new_dict)
# copy using dict() const
new_dict = dict(d)
print(new_dict)

# extend the dictionary using update method
new_dict = dict(a="alpha", b='bravo', c='charlie', d='delta', e='echo')
new_dict.update(d)
print(new_dict)

# replace values using update()
new_dict = dict(a="alpha", b='bravo', c='charlie', d='delta', e='echo')
new_dict.update({'a': 'alfa', 'f': 'fox'})
print(new_dict)

# dict are iterable
for key in new_dict:
    print("{key} => {value}".format(key=key, value=new_dict[key]))

# iterate over values
for value in new_dict.values():
    print(value)

# iterate over keys
for key in new_dict.keys():
    print(key)

# iterate over key value pair
for key, value in new_dict.items():
    print('{key} => {value}'.format(key=key, value=value))

# del using a key
del new_dict['e']
print(new_dict)

# mutablity
# keys are immutable, values are mutable
m = {'H': [1, 2, 3],
     'He': [4, 5],
     'Li': [6, 7],
     'Be': [8, 9, 10],
     'B': [11, 12],
     'C': [13, 14, 15]}
m['H'] += [16, 17]
print(m)
m['N'] = [18, 19, 20]
print(m)