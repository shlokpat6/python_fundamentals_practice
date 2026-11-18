# Exercise 12. List Comparison and Boolean Logic
'''Practice Problem: Write a function to return True if the first and last number of a 
given list is the same. If the numbers are different, return False.
'''

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def compare_ends(my_list):
    if my_list[0] == my_list[-1]:
        return True
    else:
        return False 
    
result = compare_ends(numbers_x)
print(result)
result = compare_ends(numbers_y)
print(result)
