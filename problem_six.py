# Exercise 6. Calculating Factorial with a Loop
'''Practice Problem: Write a program that calculates the 
factorial of a given number (e.g., 5!) using a for loop.'''
number = 5
total = 1

for i in range(number,0,-1):
    total = total * i

print(f"The factorial of {number} is {total}")