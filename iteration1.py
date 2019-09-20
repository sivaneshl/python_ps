def get_first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        return "Iterable is empty"


# using list
print(get_first(['1st', '2nd', '3rd']))

# using set
print(get_first({'1st', '2nd', '3rd'}))

# using empty set
print(get_first(set()))
