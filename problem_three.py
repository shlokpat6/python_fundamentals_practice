# Exercise 3. String Indexing and Even Slicing
'''Practice Problem: Display only those characters which are present at an even index number in given string.'''
user_input = input("Enter a string: ")

print("Printing only even index chars")
for i in range(len(user_input)):
    if i % 2 == 0:
        print(user_input[i])

# Note, this could have been solved via list slicing.
# Start at 0 and go to the end by skipping 2 letters
# even_letters = user_input[0::2]