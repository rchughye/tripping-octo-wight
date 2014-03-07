# Euler Problem #5: Smallest multiple
# http://projecteuler.net/problem=5
# Q: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# A: 232792560

# 2 3 5 7 11 13 17 19 (primes to 20)
# The smallest multiple will be a product of all the prime factors up to 20 with some factors repeated.
# The number of each factor in the product will the be maximum number of times that each factor occurs in any given number from 1 to 20

# Generalizable method given a list of primes up to the largest number:
# record the maximum number of times each prime occurs in any given prime factorization
# In this example, only 2,3,5,7 will be repeated more than once

#initialize
primes = [2,3,5,7,11,13,17,19]
occurences = [1,1,1,1,1,1,1,1] # of times each factor is used
temp = 0
product = 1

for num in range(2,21):
    temp = num
    #iterate through all primes
    for index in range(8):
        counter = 0
        #while divisible by prime, divide, add 1 to counter
        while temp % primes[index] == 0: 
            temp = temp / primes[index]
            counter += 1
        #if occured more times than current maximum, then update max for that prime
        if occurences[index] < counter:
            occurences[index] = counter

#print occurences

import math
for index in range(8):
    product = product * math.pow(primes[index],occurences[index])

print product
