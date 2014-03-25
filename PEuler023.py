# Euler Problem #23: Non-abundant sums
# http://projecteuler.net/problem=23
# Q: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# A: 4179871

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# All integers greater than 28123 can be written as the sum of two abundant numbers.

# from: http://mathschallenge.net/index.php?section=problems&show=true&titleid=even_sum_of_two_abundant_numbers
# Every even n >= 48 can be written as the sum of two abundant numbers


# Make list of all abundant numbers. Then flag the following:
# all odd pairwise sums.
# all even n >= 48
# all even pairwise sums n <48
# Sum the remaining values

# borrow code for divisors from P 21

import math # for sqrt function

# sum_divisors: int >= 2 -> int
# outputs the sum of all the proper divisors of a provided positive integer > 2
# no error exceptions for num < 2
# sum_divisors(220) = 284
# sum_divisors(284) = 220

def sum_divisors(num):
    divisors = []
    for d in range(1,int(math.sqrt(num))+1): # when checking divisors, only need to go up to sqrt(num)
        if num % d == 0:
            divisors += [d]
            if num/d != d: # avoid duplicates of squares
                divisors += [num/d]
    return (sum(divisors) - num) # num is not a proper divisor

#########################
#########################

# Initialize
a_sums = []
a_even = []
a_odd = []
total = 0
flags = [True] * 28124 # let flag[i] represent the flag for number i

# List of abundant numbers up to 28123

for n in range(1,28124):
    if sum_divisors(n) > n:
        if n % 2 == 0:
            a_even.append(n)
        else:
            a_odd.append(n)
            
# Generate all odd pairwise sums; must consist of 1 odd number and 1 even number 
# Assuming possible duplicates; must store sums to check for duplicates

for o in a_odd:
    for e in a_even:
        temp_sum = o + e
        if temp_sum > 28123: # since ascending lists
            break
        flags[temp_sum] = False

# even n >= 48
for i in range(48, 28123,2):
    flags[i] = False

# find even pair sums < 48
# only iterate through even since first odd abundant value is >900

for e in a_even:
    for j in a_even:
        temp_sum = e+j
        if temp_sum > 48:
            break
        flags[temp_sum] = False
        
# Total
for i in range(28124):
    if flags[i] == True:
        total += i
        
print total
