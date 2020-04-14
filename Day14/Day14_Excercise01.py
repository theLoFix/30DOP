# Rewrite the following piece of code using a context manager:

# f = open("hello_world.txt", "w")
# f.write("Hello, World!")
# f.close()

with open("Day14/hello_world.txt", "w") as f:
    f.write("Hello, World!")

# Use append mode to write "How are you?" on the second line of the hello_world.txt file above.

with open("Day14/hello_world.txt", "a") as f:
    f.write("\nHow are you?")
