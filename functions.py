students = []

# students = ["Mark", "Kate"]


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.title())
    return students_titlecase


def add_student(name):
    students.append(name)


add_student("Mark")
add_student("Kate")
add_student("Joe")

student_list = get_students_titlecase()

print(student_list)


