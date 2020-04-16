# Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movie = {key: value.title() for key, value in movie.items() }
print(movie)