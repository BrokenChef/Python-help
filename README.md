# Python-help
Generate a list of random numbers based on input from the user


# printRandomNumbers.py
# This program collects info from the user than prints out a designated amount of random numbers from the designated range 
# Darren Gilbert

import random

print('Enter the number of random numbers to be printed: ')
n = input()
print('Enter the number you want to use for the lower limit of the range')
low = input()
print('Enter the number you want to use for the upper limit of the range')
high = input()
print()
print('Random numbers between ' + low + ' ' + high + ' ' + 'are: ')
for i in range(n):
    print(random.randint(low,high))
    
    
    
    This gives errors regarding int vs str but I'm not sure how to correct it so that it works
    I just started this Python class, have no idea what I'm doing and there is NO instruction whatsoever... 
    it's just read the book then he gives us programs to write.
    
    here are the directions:
    
    
    Using the following guidelines, create a python program.
1. Create a program named printRandomNumbers that gets input from the user and then produces a list of random numbers.
2. Import the random module
3. Add three comment lines at the top of the program that contain:
a. Program Name
b. Program Description
c. Programmer's Name (You)
4. Prompt the user for the following:
a. Number of random numbers required
b. Lower limit of random numbers
c. Upper limit of random numbers
5. Using a for loop and the random.randint() method, print out a list of random numbers.
6. Submit the printRandomNumbers.py file into the Chapter 2 Assignment 3 Submission Folder.
Hints
1. See example of using the random.randint() method on page 57 (47 in 2nd Edition).
2. Remember that the values entered by the user will be strings that must be converted to integers.
    
