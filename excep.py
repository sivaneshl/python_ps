# exceptions
student = {
    "name" : "Mark",
    "student_id" : 15636,
    "course" : "python"
}
student["last_name"] = "Waugh"
last_name = None
try:
    last_name = student['last_name']
    format_last_name = 4 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("Can't add")
    print(error)
# except Exception:
#     print("Geneirc exception")
print(last_name)
