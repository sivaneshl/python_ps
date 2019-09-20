from student import Student

# HighSchoolStudent is a derived class of Student
class HighSchoolStudent(Student):  #inherit Student
    school_name = "Python High School"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
