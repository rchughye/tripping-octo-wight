# Euler Problem #21: Amicable numbers
# http://projecteuler.net/problem=21
# Q: Evaluate the sum of all the amicable numbers under 10000.
# A: 31626

# Iterate through the sum of divisors for 1 - 9999
# sum if both sum of divisors(sum of divisors) = i AND if sum of divisors != i
# i.e. if d(d(a)) = a  and d(a) != a , add a to total

# Initialize
total = 0

# Borrowing Code from problem 12 to find divisors

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

#if d(d(a)) = a  and d(a) != a , add a to total
for i in range(2,10000):
    if sum_divisors(sum_divisors(i)) == i and sum_divisors(i) != i:
        total += i
        
print total

# can improve efficiency by summing the amicable pair as well and skipping the summing of the divisors for the next iteration, as it is an O(sqrt(n)) operation
# would require more lines of code, however, and does not reduce O() runtime of script
