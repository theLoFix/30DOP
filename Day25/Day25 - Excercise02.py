# Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or lowercase).
# Hint: You should look at the constants in the string module. Documentation can be found here.
from string import ascii_letters

def have_constans(test_string):
    for character in test_string:
        if character not in ascii_letters:
            return False
        else:
            return True
