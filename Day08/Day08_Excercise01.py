# Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

play_a_game = True
number = 47

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
