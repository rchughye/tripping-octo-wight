# Euler Problem #28: Number spiral diagonals
# http://projecteuler.net/problem=28
# Q: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# A: 669171001

# Properties:
# a 1001 x 1001 spiral contains 1002001 elements, with 1002001 being on the top right most diagonal.
# Starting with 1, the first differences between diagonal elements are: 
# 2,2,2,2,4,4,4,4,6,6,6,6 ...

# Steps:
# Iterate through the spiral summing the diagonal elements 

# initialize
total = 1
element = 1 # Value of the element that will be added
f_diff = 2 # Current value for the first difference
counter = 0 # Number of times the first difference has been added

while element < 1002001: # terminate when the last number added is 1002001
    while counter != 4:
        element += f_diff
        total += element 
        counter += 1
    counter = 0
    f_diff += 2
    
print total
