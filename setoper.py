blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# blue eyes or blond hair or both
print(blue_eyes.union(blond_hair))      # blond_hair.union(blue_eyes)

# blue eyes and blond hair
print(blue_eyes.intersection(blond_hair))   # blond_hair.intersection(blue_eyes)

# blond hair without blue eyes
print(blond_hair.difference(blue_eyes))

# blue eyes or blond hair but not both
print(blue_eyes.symmetric_difference(blond_hair))   # blond_hair.symmetric_difference(blue_eyes)

# check if subset
print(smell_hcn.issubset(blond_hair))

# check if superset
print(taste_ptc.issuperset(smell_hcn))

# check if 2 sets have no members in common
print(a_blood.isdisjoint(b_blood))


