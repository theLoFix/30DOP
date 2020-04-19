# Imagine you have a file named data.txt with this content: 
#       There is some data here!

try:
    file = open("Day19\\data.txt", "r")
except FileNotFoundError as nofile:
    print("File not found")
    print(nofile)
else:
    print(file.readline())
