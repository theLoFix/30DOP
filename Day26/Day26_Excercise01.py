# Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt the user to provide information for each of these fields and create an instance of the Movie tuple you defined.
from collections import namedtuple

Movie = namedtuple("Movie", ["title", "director", "year", "budget"]) 

movie01 = Movie("Titanic", "Ridley Scott", "1990", "1000000")

print(*movie01)
