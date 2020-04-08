# Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

word = "Python"
i = 0
while i < len(word):
    if (word[i] == "o"):
        i += 1
        continue
    else:
        print(word[i])
        i += 1
