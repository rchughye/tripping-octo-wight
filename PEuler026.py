# Euler Problem #26: Reciprocal cycles
# http://projecteuler.net/problem=26
# Q: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# A: 983

# Iterate through d 1-999 and output d that provides the longest recurring cycle
# Do not need to consider any d for which the fraction terminates
# i.e do not consider d which has only prime factors of 2 or 5

# To find how long the repeating cycle of decimals are from:
# http://mathforum.org/library/drmath/view/55869.html
# Write the denominator in the form d = 2^a * 5^b * M
# Find p such that 10^p mod M is equal to 1
# As seen in long divison, when the remainder is 1 again, the decimals repeat
# any factors of 2 and 5 cause a non-repeating portion


# Initialize
longest = 0 # largest value of p
reduced = 1 # temp value that will be reduced to M
p = 1 # power of 10

for i in range(1,1000):
    reduced = i
    # first remove factors of 2 and 5
    while reduced % 2 == 0 or reduced % 5 == 0:
        if reduced % 2 == 0:
            reduced = reduced / 2
        elif reduced % 5 == 0:
            reduced = reduced / 5
    if reduced == 1: # skip non-repeating decimals
        continue
        
    # find the value of p s.t. 10^p mod M = 1
    # iteratively calculate the remainder to avoid calculating large numbers when p is large
    # i.e. do long division to avoid working with 10 ^ 300

    remainder = 10
    p = 1
    while remainder != 1:
        remainder = (remainder * 10) % reduced 
        p += 1
    
    if p > longest:
        longest = i

print longest
