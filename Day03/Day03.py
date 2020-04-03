# Strings contcatenation

""" hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: " + hourly_wage)
# print(hourly_wage)

print("Hours worked: " + hours_worked)
# print(hours_worked)
 """

age = 28

print("My age is " + str(age))

text = "{} is {} years old".format("Michal", 24)
print(text)


text = "{0} is {1} years old. and his friend {0}".format("Michal", 24)
print(text)

text = "{name} is {age} years old. and his friend {name}".format(name="Michal", age=24)
print(text)

name = "John"
age = 84

text = f"{name} is {age} years old. and his friend {name}"
text2 = text.capitalize()
print(text2)


text3 = "  START this is wrongly formated text with name in it   END   "
print(text3)

text3 = text3.strip()
print(text3)
