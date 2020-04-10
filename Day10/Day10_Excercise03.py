# Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
# If you use a different album for the exercises, update the date accordingly.

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
