# Exercise 2. Cumulative Sum of a Range
'''Practice Problem: Iterate through the first 10 numbers (0–9). 
In each iteration, print the current number, the previous number, and their sum.'''

def sum_of_range():
    previous_number = 0
    for i in range(10):
        print(f"Current Number {i} Previous Number {previous_number} Sum: {previous_number+i}")
        previous_number = i

sum_of_range()