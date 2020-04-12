#  Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

new_set = set()
new_set.update(["one", "two", "three"])

print(new_set)
new_set.add("four")

print(new_set)

second_set = {"four", "one", "five", "six"}
print(second_set)

third_set = new_set.union(second_set)
print(third_set)

fourth_set = new_set.difference(second_set)
print(fourth_set)

fifth_set = new_set.symmetric_difference(second_set)
print(fifth_set)

sixth_set = new_set.intersection(second_set)
print(sixth_set)
