# Euler Problem #12: Highly divisible triangular number
# http://projecteuler.net/problem=12
# Q: What is the value of the first triangle number to have over five hundred divisors?
# A: 76576500

# Triangular number is the sum of the arithmetic series
# closed form  Sn = n(n+1)/2
# Process: Get Triangle number, find divisors, check if greater than 500 divisors, repeat
# Note: the below method seems to be somewhat inefficient, took approx 30 seconds to process
# is O(n^2) runtime currently, reduced from O(n^3) by noting one only has to go to sqrt(T_num) when checking for divisors
# Would not terminate in a reasonable time unless efficiency improved.

# Initialize
T_num = 1
flag = False
counter = 1
divisors = []

import math # for sqrt function

while flag == False:
    T_num = counter * (counter + 1) / 2
    divisors = []
    for d in range(1,int(math.sqrt(T_num+1))): # when checking divisors, only need to go up to sqrt(T_num)
        if T_num % d == 0:
            divisors += [d]
            divisors += [T_num/d]
    if len(divisors) > 500:
        flag = True
        #print divisors
    counter += 1
    #if counter >= 10000:
        #print counter
        #print divisors
        #print len(divisors)
        #break

print T_num   
