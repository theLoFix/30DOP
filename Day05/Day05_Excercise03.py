# Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

number = float(input("Please provide some number... "))

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is ZERO")
else:
    print(f"{number} is negative")
