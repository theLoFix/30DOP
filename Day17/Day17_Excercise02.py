# Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def showme(*args,**kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("Keywords arguments:")
    for key,value in kwargs.items():
        print(f"{key}: {value}")


showme(1,2,3,title="Tato",director="Reżyser")
