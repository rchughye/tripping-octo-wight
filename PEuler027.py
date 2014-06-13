# Euler Problem #27: Quadratic primes
# http://projecteuler.net/problem=27
# Q: Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
# A: -59231

# Considering quadratics of the form: n² + an + b, where |a| < 1000 and |b| < 1000

# Useful properties:
# Since n must start at 0, b must be positive and prime

# Steps:
# Iterate over all b, a to find which provides the maximum number of consecutive primes.
# Store the values of a and b which provide the max number of primes.
# Output the product of these values of a and b. 

# Borrow code from problem 10 for primes

# primes: int >= 1 -> [list of primes]
# takes natural number n and outputs a list of primes up to n
# uses the Sieve of Eratosthenes method.
# primes(7) -> [2,3,5,7]

def primes(n):
    import math
    Prime_Flags = [True] * n
    Prime_Flags[0] = False #1 is not prime
    Primes = []
    
    for index in range(1,int(math.sqrt(n))+1): #only need to go up to sqrt n
        if Prime_Flags[index-1] == True:
            for i in range(index*index,n + 1,index): # for all multiples of p up to n
                Prime_Flags[i-1] = False
    
    for i in range(n):
        if Prime_Flags[i] == True:
            Primes += [i+1]
    return Primes

# is_prime: int >=2 -> bool
# outputs True if n >=2 is prime, False otherwise
# is_prime(2) -> True
# is_prime(4) -> False
def is_prime(n):
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#####
#####
import math

# Initialize
n = 0
longest = 0
q = 0 # value of n*n + a * n + b
a_max = 0
b_max = 0

# Iterate over all possible values
for b in primes(1000):
    for a in range(-999,1000):
        n = 0
        while True:
            q = n*n + a * n + b
            if is_prime(math.fabs(q)):# take absolute value to deal with negative values
                n += 1
            else:
                break
        if n > longest:
            longest = n
            a_max = a
            b_max = b

print a_max * b_max
        
