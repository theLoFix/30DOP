# Unpack the following tuple into 4 variables:
# The data represents a student's name, their student id number, and their major and minor disciplines in that order.

data = ("John Smith", 11743, ("Computer Science", "Mathematics"))

# student_name = data[0]
# student_id = data[1]
# major_disciplines = data[2][0]
# minor_disciplines = data[2][1]

student_name, student_id, (major_disciplines, minor_disciplines) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

print(student_name)
print(student_id)
print(major_disciplines)
print(minor_disciplines)