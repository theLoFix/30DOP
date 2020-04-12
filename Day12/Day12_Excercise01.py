# Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.
# When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.
# You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.

def add(arg1, arg2):
    print(arg1 + arg2)


def subtract(arg1, arg2):
    print(arg1 - arg2)


def devide(arg1, arg2):
    if arg2 == 0:
        print("You can't devide by 0!")
    else:
        print(arg1 / arg2)


def multiply(arg1, arg2):
    print(arg1 * arg2)


add(2, 4)
subtract(4, 2)
devide(4, 2)
devide(4, 0)
multiply(2, 4)
