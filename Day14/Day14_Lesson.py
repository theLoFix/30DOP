# file open
file_path = "Day14\example.txt"

file = open(file_path, "r")
print(file.read())
file.close()

with open(file_path, "a") as file2:
    file2.write("Taka dodatkowa linia.\n")
