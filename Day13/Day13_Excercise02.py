#  Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

def process_string (string):
    new_string = str(string).lower().replace(" ", "")
    return new_string


print(process_string("Ala ma kota"))
