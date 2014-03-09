# Euler Problem #10: Summation of primes
# http://projecteuler.net/problem=10
# Q: Find the sum of all the primes below two million.
# A: 142913828922

# Step 1: Find primes and store them
# Use the Sieve of Eratosthenes method, iteratively eliminating multiples of the next prime numbers
# i.e. find all primes in a certain range by eliminating all composite numbers

Prime_Flags = [True] * 2000000
Prime_Flags[0] = False #1 is not prime
Primes = []

for index in range(1,1416): #only need to go up to sqrt 200000 = 447.21
    if Prime_Flags[index-1] == True:
        for i in range(index*index,2000001,index): # for all multiples of p up to 2000000
            Prime_Flags[i-1] = False

for i in range(2000000):
    if Prime_Flags[i] == True:
        Primes += [i+1]
        
print sum(Primes)
