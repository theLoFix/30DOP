# Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user when the values they entered cannot be converted.

user_input = input("Provide list of grades separated by commas: ").strip().lower().split(",")

# grades = [int(grade) for grade in user_input]

try:
    grades = [int(grade) for grade in user_input]
except ValueError: 
    print("One of values is wrong!")
