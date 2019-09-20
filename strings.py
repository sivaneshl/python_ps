# str - immutable

print(len("ajsajo lijco ajdo"))     # length

print("new" + "found" + "land")     # concatenate

s = "New"
s += "found"
s += "land"
print(s)

# join operator
colors = ';'.join(['blue', 'red', 'green', 'black'])    # operator on the separator; list of strings to be joined as args
print(colors)
print(colors.split(';'))        # split using separator

# concatenate collection of strings - join using empty string operator
text = ''.join(["new", "found", "land"])
print(text)

# partition
print("unforgetable".partition("forget"))   # partition the string "unforgetable" using the seperator as  "forget"

# partition returns a tuple
# can be unpacked
departure, sep, arrival = "London:Edinburg".partition(":")
print(departure, sep, arrival)

origin, _, destination = "London-Edinburg".partition("-")   # _ is for unused or dummy variables
print(origin, arrival)

# format
print("The age of {0} is {1}".format("James", 33))
print("Current position is {lat} {long}".format(lat="60N", long="5E"))

# format
pos = (65.2, 23.1, 82.2)
print("x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos))

# format can also be used from import
import math
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))



