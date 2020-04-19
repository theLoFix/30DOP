# Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.

user_input = input("Provide list of grades separated by commas: ").strip().lower().split(",")

# grades = [int(grade) for grade in user_input]

try:
    grades = [int(grade) for grade in user_input]
    return grades
except ValueError: 
    print("One of values is wrong!")
finally:
    return grades

print(type(grades))