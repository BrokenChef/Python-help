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