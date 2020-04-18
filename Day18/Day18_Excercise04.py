# Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

from random import randint as rnd

play_a_game = True
number = rnd(1,100)

while play_a_game:
    user_guess = int(input("Please guess a number form 1 to 100: "))

    if user_guess == number:
        print("You WON!")
        play_a_game = False
    elif user_guess > number:
        print("Your number is higher, guess again!")
    else:
        print("Your number is lower, guess again!")

print("CONGRATULATIONS you WON, GAME OVER.")
