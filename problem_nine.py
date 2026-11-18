# Exercise 9. Vowel Frequency Counter
'''Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) 
present in a given sentence.'''
vowels = ["a","e", "i", "o", "u"]
sentence = "Learning Python is fun!"
count = 0
for i in sentence:
    if i in vowels:
        count += 1
print(count)