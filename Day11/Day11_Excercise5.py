#  Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

numbers = set(range(47, 56))
print(numbers)

check = True

while (check):
    guess = int(input("Guess a number? "))
    if guess in numbers:
        print(f"{guess} is in th range")
        check = False
    else:
        print(f"You're WRONG, {guess} so not in range")
