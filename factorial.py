#Write a Python script to calculate the factorial of a given number using a loop
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