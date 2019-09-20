# dictionary
student = {
    "name" : "Mark",
    "student_id" : 15636,
    "course" : "python"
}

# list of dictionary
students = [
    {"name" : "Mark", "student_id" : 15636},
    {"name" : "James", "student_id" : 15637},
    {"name" : "Jessica", "student_id" : 15638}
]

print(students)

print(student.keys())
print(student.values())

# keyerror
print(student['name'])
print(student['lastname'])
