# Remove the first movie from movies. Use any method you like.

movie = [("Szeregowiec Ryan", "Steven Spillberg", 1998)]

new_title = input("Please provide title of your favourite film: ")
new_director = input("Who direct this film? ")
new_date = input("At what year it was produced? ")

new_tuple = (new_title, new_director, new_date)

print(movie)
movie.append(new_tuple)
print(movie)

movie.pop(0)
print(movie)

print(f'Your favourite movie is "{movie[0][0]}", directed by {movie[0][1]} in {movie[0][2]}.')
