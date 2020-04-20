# Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.

positive_numbers = filter (lambda number: number >= 0, range(-5, 11))

print(*positive_numbers, sep="\n")
