# Try to use the is operator or the id function to investigate the difference between this:

a = numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

# And this:

b = numbers = [1, 2, 3, 4]
d = numbers.append(5)

print(a is b)
print(id(a))
print(id(b))
print(id(new_numbers))
print()
