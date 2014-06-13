# Euler Problem #30: Digit fifth powers
# http://projecteuler.net/problem=30
# Q: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# A: 443839

# Properties:
# A single digit is not considered to be a sum. There must be at least 2 digits.
# 9 ^ 5 = 59049
# Since the sum of fifth powers for 999999 -> 354294, an upper bound is any 7 digit number by inspection

# Brute force:
# Express numbers in string form, then check each digit for its power
# if a number can be written as the sum of fifth powers of their digits, add to the counter

# Initialize
s = "" # temp value of string representation
temp_sum = 0 # temp value of each sum of fifth powers
total = 0

for i in range(11,1000001):
    s = str(i)
    temp_sum = 0
    for l in s:
        temp_sum += int(l) ** 5
    if temp_sum == i:
        total += temp_sum
        
print total
