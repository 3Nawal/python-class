a = 10
print("Type of a: ", type(a))
b = 10.5
print("Type of b: ", type(b))
c = 10 + 5j
print("Type of c: ", type(c))

string1 = "Hello"
string2 = 'World'
string3 = '''
The snow in the mountains was melting and Bunny had been dead for several weeks before we came to understand the gravity of our situation.'''

print(string1 + " " + string2 + " " + string3)
print("Type of string1: ", type(string1))
print("Type of string2: ", type(string2))
print("Type of string3: ", type(string3))

list_var = []
print("initial blank list: ", list_var)
print("Type of list: ", type(list_var))

list_var = ['Geeks', 'For', 'Geeks']
print("List with the use of string: ", list_var)
list_var = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# creating a tuple using assignment of values
tuple1 = ()
print("The type of tuple1: ", type(tuple1))
tuple1 = (1, "Geeks", 'a')
print("tuple1: ", tuple1)
print("First item in tuple1: ", tuple1[1])
tuple2 = ("First item in tuple1", tuple1[1])

print("Type of keyword True: ", type(True))
print("Type of keyword False: ", type(False))
print("Type of keyword None: ", type(None))

set1 = set("This is a set with a string")
set2 = {1, "string", True}
print("Type of set1: ", type(set1))
print("content of set1: ", set1)
print("Type of set2: ", type(set2))
print(set2)
for i in set2:
    print(i)

Dictionary1 = {1: "Geeks", 2: "For", 3: "Geeks"}
Dictionary2 = {'Name': "Bunny", 'Age': 20, 'Gender': "Male", 'Alive': False}
print("Type of Dictionary1: ", type(Dictionary1))

# access the items using types of keys
print("The Dictionary2 Name: ", Dictionary2['Name'])
print("The Dictionary2 Age: ", Dictionary2['Age'])

num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print(num, "is neither positive nor negative, it is ZERO")
else:
    print(num, "is a negative number.")

sum_var = 0
list_var = (6, 5, 3)
for i in list_var:
    sum_var += i
print("The sum of the list is: ", sum_var)

lista = list(range(10))
print("print the whole lista: ", lista)

listb = list(range(1, 10, 2))
print("print the whole listb: ", listb)

listc = list(range(0, 10, 2))
print("print the whole listc: ", listc)

sum_var = 0
for i in range(1, 10):
    sum_var += i
print(sum_var)

x = range(6)
for n in x:
    print(n)

meow = ["bunny", "flo", "owl"]
for i in meow:
    print(i)


i = 10  # Define i before using it
if i > 9:
    print("finally")
else:
    print("Not greater than 9")

k = 1.6
if k > 9:
    print("finally")
elif k >= 1.6:
    print("NO")
else:
    print("YOO")

sum_var = 0
i = 1
while i <= 10:
    sum_var += i
    print("the sum of the first", i, "natural numbers is: ", sum_var)
    i += 1
print("great success")

for val in "string":
    print('in loop', val)
    if val == "i":
        break
print('out of loop', val)

for char in "string":
    print('in loop', char)
    if char == "i":
        print('i found', char)
print('out of loop', char)

sequence = [1, 2, 3, 4, 5]
for val in sequence:
    pass

print("The end")

def greet(name):
    '''
    This function greets the person
    using the name passed as a parameter
    '''
    print("Hello " + name + ". Nice to meet you.")
greet("Ash")
greet("E")

print(greet.__doc__)

def add(a, b=0):
    return a + b
print("The sum =", add(2))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Welcome to the Factorial Calculation Program!")
while True:
    try:
        num = int(input("Enter a positive integer to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers. Please enter a positive integer.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
            break
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

class Employee:
    def __init__(self, empID=999, first='Jane', last='Doe', pay=0.00):
        self.empID = empID
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        print(f"Employee created: {self.fullname()} | ID: {self.empID} | Pay: {self.pay} | Email: {self.email}")

    def fullname(self):
        return self.first + ' ' + self.last

# Creating employee objects and printing their details
emp1 = Employee()
emp2 = Employee(100, 'Paula', 'Musuva', 1000.00)

# Printing employee details
print(f"Full Name of emp1: {emp1.fullname()}")
print(f"Full Name of emp2: {emp2.fullname()}")

class Parent:
    parentAttr = 100
    
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr
        print(f"Setting Parent Attribute to: {attr}")

    def getAttr(self):
        print("Parent Attribute: ", Parent.parentAttr)

# Creating Parent object
p = Parent()

# Calling Parent methods
p.parentMethod()
p.setAttr(200)
p.getAttr()