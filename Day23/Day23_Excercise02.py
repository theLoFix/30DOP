# Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.


names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)

names = (name.strip().title() for name in names)

print(next(names))
print(next(names))
print(next(names))
