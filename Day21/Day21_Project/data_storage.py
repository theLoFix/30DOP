
def read_column(number):
    column_data = []
    with open("Day21\\Day21_Project\\iris.csv", "r") as iris:
        for line in iris.readlines()[1:]:
            data = line.strip().split(",")
            column_data.append(data[number])

    return column_data
