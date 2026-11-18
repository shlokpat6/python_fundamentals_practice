# Exercise 1. Arithmetic Product and Conditional Logic
'''Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product;
 otherwise, return their sum.'''

user_input1 = int(input("Enter the first number: "))
user_input2 = int(input("Enter the second number: "))

def check_arithmetic(num1, num2):
    if (num1 * num2) <= 1000:
        return num1 * num2
    else:
        return num1 + num2

print(check_arithmetic(user_input1, user_input2))

# From a mistake- remember that input returns a string, so need to convert to int for arithemetic