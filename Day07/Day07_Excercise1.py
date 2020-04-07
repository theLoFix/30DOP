# Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

answer = (input("Please provide your first and last name... ")).split()
print(answer)

first_name = answer[0]
last_name = answer[1]

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
