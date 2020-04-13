# 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:

# ("Tom Hardy", "English", 42)  # name, nationality, age


def convertToDict(tuple):
    new_dictionary = { "name": tuple[0], "nationality" : tuple[1], "age" : tuple[2] }
    return new_dictionary


var = convertToDict(("Tom Hardy", "English", 42))
print(var["name"])


for key, value in var.items():
    print(f"{key}:{value}")
