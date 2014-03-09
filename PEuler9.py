# Euler Problem #9: Special Pythagorean triplet
# http://projecteuler.net/problem=9
# Q: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# A: 31875000

# Iterate through all pairs of c and (a+b) which sum to 1000. Print answer when a^2 + b^2 = c^2
# Initialize
answer = 0

for c in range(1,1000):
    for a in range(1,1001-c):
        b = 1000 - a - c
        a2 = a*a
        b2 = b*b
        c2 = c*c
        if c2 == a2+b2:
            answer = a*b*c
            print answer
            #print a
            #print b
            #print c
            break
