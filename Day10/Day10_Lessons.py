movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}

meta_info = {
	"runtime": 181,
	"budget": "$356 million",
	"earnings": "$2.798 billion",
	"producer": "Kevin Feige"
}
print(movie)

movie.update(meta_info)

print(movie)
movie["producer"] = "Lukasz Zawadzki"
print(movie)

for attribute in movie:
    print(attribute)

for value in movie.values():
    print(value)

for key, value in movie.items():
    print(f"{key} with {value}")
