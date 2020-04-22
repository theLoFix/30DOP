#  Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up the shop at night. This means that for employees A, B, and C, employee A will close the shop on day 1, then B will close the shop on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.

# Write a program to create a schedule that lists which of your employees will lock up the shop on a given day over a 30 day period. You should list the day number, the employee name, and the day of the week. You can choose any employee to lock the shop on day 1, and you can also choose which day of the week day 1 corresponds to.

# You should make use of the cycle function in the itertools module to create a repeating series of values.

from itertools import cycle

employees = cycle(["Piotr","Bożena", "Cyceron"])
weekday = cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
day_of_week = range(1,31)

#schedule = zip(day_of_week, cycle(employees))
#print (*schedule, sep="\n")

for day in day_of_week:
    print(f"Day {day} ({next(weekday)}): {next(employees)} closes.")
