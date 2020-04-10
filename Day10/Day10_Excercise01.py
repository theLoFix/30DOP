# Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then another tuple containing the track list.
# Convert this outer tuple to a dictionary with four keys.

tuple1 = (
 	"The Dark Side of the Moon",
 	"Pink Floyd",
 	1973,
 	(
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
 )
print(tuple1)

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

print(album)
