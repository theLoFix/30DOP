# Use the sort method to put the following list in alphabetical order with regards to the students' names:

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]


students.sort(key=lambda el: el["name"])


for item in students:
    print(item)
