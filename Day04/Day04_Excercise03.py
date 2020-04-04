# Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.

movie = [("Szeregowiec Ryan", "Steven Spillberg", 1998)]

new_title = input("Please provide title of your favourite film: ")
new_director = input("Who direct this film? ")
new_date = input("At what year it was produced? ")

new_tuple = (new_title, new_director, new_date)

movie.append(new_tuple)

print(movie)
print(movie[1][1])
