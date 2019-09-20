from pprint import pprint as pp

# mutablity
# keys are immutable, values are mutable
m = {'H': [1, 2, 3],
     'He': [4, 5],
     'Li': [6, 7],
     'Be': [8, 9, 10],
     'B': [11, 12],
     'C': [13, 14, 15]}
m['H'] += [16, 17]
pp(m)
m['N'] = [18, 19, 20]
pp(m)