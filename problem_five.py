# Exercise 5. Variable Swapping (The In-Place Method)
'''Practice Problem: Write a program to swap the values of two variables, a and b, 
without using a third temporary variable.'''

input1 = int(input("Enter a number: "))
input2 = int(input("Enter another number: "))
print(f"Before swap a = {input1}, b = {input2}")
input1, input2 = input2, input1
print(f"After swap a = {input1}, b = {input2}")