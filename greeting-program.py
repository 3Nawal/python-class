#greeting program
def greet(name):
    '''
    This function greets the person
    using the name passed as a parameter
    '''
    print("Hello " + name + ". Nice to meet you.")

greet("Ash")
greet("E")

print(greet.__doc__)