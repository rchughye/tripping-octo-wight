# Euler Problem #4: Largest palindrome product
# http://projecteuler.net/problem=4
# Q: Find the largest palindrome made from the product of two 3-digit numbers.
# A: 906609

# Start at 999 x 999 and work backwards from that, checking if each product is a palindrome
# store all palindromes, check maximum of list

# Checking if a palindome:
# Product will necessarily have a maximum of 6 digits (999^2 = 998001)

# Pal_Checker: int -> bool
# Outputs true if an input integer is a palidrome, false otherwise
# Will currently hardcode for positive integers with 6 digits ONLY as that is the expected size for this question
# Examples: Pal_Checker(111111) -> True, Pal_Checker(111110) -> False

def Pal_Checker(val):
    d1 = val / 100000
    d2 = (val % 100000) / 10000
    d3 = (val % 10000) / 1000
    d4 = (val % 1000) / 100
    d5 = (val % 100) / 10
    d6 = (val % 10)
    if d1 == d6 and d2 == d5 and d3 == d4:
        return True
    else:
        return False

#initialize
l1 = range(999,500,-1)
pals = [0]
cur = 0

for val in l1:
    for val2 in l1:
        cur = val * val2
        if Pal_Checker(cur) == True:
            pals += [cur]

print max(pals)
