#  Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.

list1 = ["Jan", "Marta", "Gons"]
tuple1 = (1, 2, 3, 4)

for imie, counter in zip(list1, tuple1):
    print(f"{imie} - {counter}")

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]


for imie, counter in zip(pet_owners, pets):
    print(f"{imie} - {counter}")
