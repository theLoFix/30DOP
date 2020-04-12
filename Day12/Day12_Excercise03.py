# Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:
# tv_show = {
#  	"title": "Breaking Bad",
#  	"seasons": 5,
#  	"initial_release": 2008
#  }
 
#  print_show_info(tv_show)
#  Breaking Bad (2008) - 5 seasons

series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

def print_show_info(data):
    print(f"{data['title']} ({data['initial_release']}) - {data['seasons']} season(s)")


for item in series:
	print_show_info(item)
