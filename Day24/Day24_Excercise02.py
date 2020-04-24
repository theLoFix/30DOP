# Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.

def divide(a, b)
	try:
		print(a / b)
	except ZeroDivisionError:
		print("Cannot divide by zero")
	except TypeError:
		print("Both values must be numbers. Cannot divide {a} and {b}")
	except ArithmeticError:
		print("Could not complete the division. The numbers were likely too large")

