# Use a defaultdict to store a count for each character that appears in a given string. Print the most common character in this dictionary.

from collections import defaultdict


word = "piedziesieciocentowka"

char_numbers = defaultdict(int)

for letter in word:
    char_numbers[letter] +=1

for key, value in char_numbers.items():
    print(f"{key}: {value}")

most_common_character = max(char_numbers, key=lambda key: char_numbers[key])

print(most_common_character)  # o
