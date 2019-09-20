students = []


class Student:

    school_name = "Python Elementary"

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

# HighSchoolStudent is a derived class of Student
class HighSchoolStudent(Student):  #inherit Student
    school_name = "Python High School"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"



james = HighSchoolStudent("james")
print(james.get_name_capitalize())