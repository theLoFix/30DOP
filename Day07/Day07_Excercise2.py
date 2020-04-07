#  Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

my_list = [1, 2, 3, 4, 5]
new_list = []
for i in range(len(my_list)):
    new_list.append(str(my_list[i]))

# print(new_list)
formated_list = " | ".join(new_list)
print(formated_list)
