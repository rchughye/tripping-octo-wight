# Euler Problem #6: Sum square difference
# http://projecteuler.net/problem=6
# Q: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# A: 25164150

# Square of sum = 5050 ^ 2 by arithmetic series

# Sum of squares get by iterating

# initialize
S = 0

for i in range(1,101):
    S += i * i

print 5050 * 5050 - S
