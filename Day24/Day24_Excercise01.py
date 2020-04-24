# Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, raise a ValueError and inform them that their choice was invalid.


answer = int(input("Please provide number from 1 to 10: "))

if (answer > 10) or (answer < 1):
    raise ValueError(f"Number {answer} is not in selected range!")
