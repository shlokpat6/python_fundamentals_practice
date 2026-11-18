# Exercise 4. String Slicing and Substring Removal
'''Practice Problem: Write a function to remove characters from a string starting from index 0 up to n 
and return a new string.'''

def truncate_string(input_string, start_index):
    truncated_list = input_string[start_index:]
    return truncated_list

user_input = input("Enter a string: ")
user_input2 = int(input("Enter a number: "))
print(truncate_string(user_input,user_input2))