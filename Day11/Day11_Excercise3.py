# Create a second set which includes at least one common element with the first set.

new_set = set()
new_set.update(["one", "two", "three"])

print(new_set)
new_set.add("four")

print(new_set)

second_set = {"four", "one", "five", "six"}
print(second_set)
