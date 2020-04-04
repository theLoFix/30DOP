# Print both movies in the movies collection.

movie = [("Szeregowiec Ryan", "Steven Spillberg", 1998)]

new_title = input("Please provide title of your favourite film: ")
new_director = input("Who direct this film? ")
new_date = input("At what year it was produced? ")

new_tuple = (new_title, new_director, new_date)

movie.append(new_tuple)

print(f'Your favourite movie is "{movie[1][0]}", directed by {movie[1][1]} in {movie[1][2]}.')
