# Use the map function to find the sum of the numbers in each tuple. Use manual iteration to print the first two results provided by the resulting map object.

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]


totals = map(sum, numbers)
print(*totals, sep="\n")

# print(next(totals))
# print(next(totals))
