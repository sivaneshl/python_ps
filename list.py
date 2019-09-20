# list.py

student_names = ["Mark", "Katrina", "Jessica"]
print(student_names)

print(student_names[1])
print(student_names[-1])  # last element

# student_names[3] = "Homer"
student_names.append("Homer")
print(student_names)

print(len(student_names))

del student_names[2]
print(student_names)

# slicing
print(student_names[1:])
print(student_names[1:-1])
