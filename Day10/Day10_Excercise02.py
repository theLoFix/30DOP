# Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.

album = {
	"album":  "The Dark Side of the Moon",
 	"artist":"Pink Floyd",
 	"year": 1973,
 	"track": (
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 }

for key, value in album.items():
	print(f"{key}: {value}")
