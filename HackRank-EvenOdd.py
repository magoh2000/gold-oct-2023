"""
Practice from HarkerRank for an even/odd checker with several conditions.
From HackerRank: 
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""

#!/bin/python3

# Import necessary modules
import math
import os
import random
import re
import sys

# Check if the script is being run as the main program

print("Enter a number: ")

if __name__ == '__main__':
    # Prompt the user for an integer input and strip any leading/trailing whitespace
    n = int(input().strip())

# Check if 'n' is odd
if n % 2 == 1:
    print('Weird')
# Check if 'n' is even and falls into one of the specified conditions
elif n > 20 or (n >= 2 or n <= 5):
    print('Not Weird')
# If 'n' is even but does not meet the above conditions, print 'Weird'
else:
    print('Weird')
