# Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:
# tv_show = {
#  	"title": "Breaking Bad",
#  	"seasons": 5,
#  	"initial_release": 2008
#  }
 
#  print_show_info(tv_show)
#  Breaking Bad (2008) - 5 seasons



tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
}

def print_show_info(data):
    print(f"{data['title']} ({data['initial_release']}) - {data['seasons']} seasons")

#print(tv_show["title"])
print_show_info(tv_show)
