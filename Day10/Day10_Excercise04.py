# Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.

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
print("\n")

del album["year"]
del album["track"]
for key, value in album.items():
	print(f"{key}: {value}")
print("\n")

album["date_of_release"] = "March 1st"
for key, value in album.items():
	print(f"{key}: {value}")
print("\n")

print(album.get("track", False))
