students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id):
    student = {"name" : name, "student_id" : student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as e:
        print("Could not save file")
        print(e)


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as e:
        print("Could not read file")
        print(e)


read_file()
print_students_titlecase()


while True:
    can_continue = input("Do you want to add a student? ")
    if can_continue == "yes":
        student_name = input("Enter Student Name: ")
        student_id = input("Enter Student ID: ")
        add_student(student_name, student_id)
        save_file(student_name)
    else:
        print_students_titlecase()
        break
