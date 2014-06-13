# Euler Problem #29: Distinct powers
# http://projecteuler.net/problem=29
# Q: How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
# A: 9183

# Brute Force:
# Utilize the fact a set will not add duplicate numbers
# add all numbers, output length of set

# Initialize
s = set()

for a in range(2,101):
    for b in range(2,101):
        s.add(a**b)
        
print len(s)
