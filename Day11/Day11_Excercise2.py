# Add three items to your empty set using either several add calls, or a single call to update.


new_set = set()

new_set.update(["one", "two", "three"])

print(new_set)
new_set.add("four")

print(new_set)
