
# Staircase detail
# This is a staircase of size :
#    #
#   ##
#  ###
# ####
# Its base and height are both equal to n. It is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.
# Write a program that prints a staircase of size n.
# Function Description
# Complete the staircase function in the editor below.
# staircase has the following parameter(s):
# int n: an integer
# Print
# Print a staircase as described above.
# Input Format
# A single integer, n, denoting the size of the staircase.
# Constraints
# 0 < n <= 100.
# Output Format
# Print a staircase of size n using # symbols and spaces.
# Note: The last line must have 0 spaces in it.
# Sample Input
# 6
# Sample Output
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# Explanation
# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n=6.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    i = 1
    j = 1
    while i<= n:
        print(" " * (n-j) + "#" * i)
        i += 1
        j += 1
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
