# Euler Problem #7: 10001st prime
# http://projecteuler.net/problem=7
# Q: What is the 10 001st prime number?
# A: 104743

# Use the Sieve of Eratosthenes method, iteratively eliminating multiples of the next prime numbers
# i.e. find all primes in a certain range by eliminating all composite numbers
# Start with range from 2 to 50000, increasing range if necessary for more primes
# Store all primes in a list, recall index 10000 for answer, which is item 10001

# More Primes were needed, double range to 100000
# More Primes were needed, double range to 200000

# Start with all numbers as True, then iteratively list multiples of next prime as false
# algorithm idea from wiki http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation

# Initialize
Prime_Flags = [True] * 200000
Prime_Flags[0] = False #1 is not prime
Primes = []

for index in range(1,449): #only need to go up to sqrt 200000 = 447.21
    if Prime_Flags[index-1] == True:
        for i in range(index*index,200001,index): # for all multiples of p up to 200000
            Prime_Flags[i-1] = False

for i in range(200000):
    if Prime_Flags[i] == True:
        Primes += [i+1]

if len(Primes) >= 10000:
    print Primes[10000]
else:
    print 'Not enough primes'
