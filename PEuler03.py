# Euler Problem #3: Largest prime factor
# http://projecteuler.net/problem=3
# Q: What is the largest prime factor of the number 600851475143 ?
# A: 6857

# Iteratively divide by increasing numbers until the value is reduced to 1
# Store factors (which can possibly be reduced further) into a list
# Repeat process on largest factor to verify it is prime

Val = 600851475143
Divider = 3 # clearly not divisible by 2 start at 3
Factors = [1]

while Val != 1:
    if Val % Divider == 0: # if divisble -> if a factor
        Val = Val / Divider
        Factors += [Divider]
    Divider += 1

print Factors
