""" For this project, your program should do the following:

Calculate the average budget of all movies in the data set.
Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
Print out how many movies spent more than the average you calculated.
If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.
 """

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

sum_of_all_budgets = 0

# calcualte summ of all budgets
for i in range(len(movies)):
    sum_of_all_budgets += movies[i][1]

avarage_budget = sum_of_all_budgets / len(movies)

for movie in movies:
    if (movie[1] > avarage_budget):
        print(f"Film '{movie[0]}'' has budget higher than avarage for {int(movie[1] - avarage_budget)}$ more.")
