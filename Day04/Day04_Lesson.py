# Lists

names = ["Jan", "Alicja", "Sara", "Grzegorz"]
print(names)

names = [
    "Jan", 
    "Alicja", 
    "Sara", 
    "Grzegorz"
    ]
print(names)

friend_details = ["Jan", 27, "Web Developer"]
print(friend_details)

names = ["Jan", "Alicja", "Sara", "Grzegorz"]
print(names[2])

names = ["Jan", "Alicja", "Sara", "Grzegorz"]
print("Moja mama ma na imię " + names[1] + ".")


names = ["Jan", "Alicja", "Sara", "Grzegorz"]
print("A mój tata ma na imię " + names[-1] + ".")


names = ["Jan", "Alicja", "Sara", "Grzegorz"]
names.append("Gons")
print("A mój tata ma na imię " + names[-1] + ".")
names = names + ["Stefan"]
print("A mój tata ma na imię " + names[-1] + ".")

names.insert(1, "Maria")
print("Moja mama ma na imię " + names[1] + ".")

names.remove("Gons")
print("A mój tata ma na imię " + names[-1] + ".")

print(names)
del names[0]
print("Moja mama ma na imię " + names[1] + ".")

inThePop = names.pop()
print("A mój tata ma na imię " + names[-1] + ".")
print("In the pop: " + inThePop)

print(names)
names.clear()
print(names)


# Tuples

movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]

print(movies[2])

print(movies[2][0])
