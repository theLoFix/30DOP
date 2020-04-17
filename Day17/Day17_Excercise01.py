# Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.

def sumon(*numbers):
    return sum(numbers)


print(sumon(1,2,3,4,5))
