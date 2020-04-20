#  Below you'll find a tuple containing several names:

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine","stanislaw")

# Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. 
# Make sure that every name in the new list is in title case.


filtered_names = [name.title() for name in names if len(name) < 8]

print(*filtered_names, sep=", ")

