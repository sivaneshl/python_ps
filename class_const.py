students = []


class Student:

    school_name = "Python"

    def __init__(self, name, student_id=332):  # constructor method
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


mark = Student("Mark")
# print(students)
print(mark)
