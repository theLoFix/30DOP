# For the employees above, print out those who are earning an hourly wage above average.
# Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
total_wage = 0
number_of_employees = 0


for entry in employees:
    total_wage += entry[1] * entry[2]
    number_of_employees += 1

avarage_wage = total_wage / number_of_employees

print("Avarage wage: ")
print(avarage_wage)

for entry in employees:
    if (entry[1] * entry[2]) > avarage_wage:
        print(f"Employee {entry[0]} earns above avarage")