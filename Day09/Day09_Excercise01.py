# The data contains the character name, the voice actor or actress who plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print each tuple in the following format:
# BoJack Horseman is a horse voiced by Will Arnet.

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for counter, (character, actor, animal) in enumerate(main_characters):
    print(f"{character} is a {animal.lower()} voiced by {actor}.")
