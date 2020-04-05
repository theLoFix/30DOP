# Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.

hours_worked_this_week = float(input("How many hours you worked this week? "))

if hours_worked_this_week > 40:
    hourly_wage = float(input("What is your whourly wedge? "))
    additional_ammount = (hours_worked_this_week - 40) * hourly_wage * 1.1
    print(f"The employee is due some additional pay in amount - {additional_ammount}")
elif hours_worked_this_week < 40:
    print("You have some underhours, you need to work some more this week!")
else:
    print("You work out your weekly norm of work houts Thank you :D")
