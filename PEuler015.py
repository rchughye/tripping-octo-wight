# Euler Problem #15: Lattice paths
# http://projecteuler.net/problem=15
# Q: How many such routes are there through a 20×20 grid?
# A: 137846528820

# The problem can be reduced to counting the number of permuations of n right movements and n down movements
# From probability/counting methods, the number of paths can be expressed as  2n choose n
# This can be reduced to 40! / (20!)^2

# Without importing factorials/math libraries:

# Initialize
top = 1
bottom = 1

for i in range(40,20,-1):
    top = top * i

for j in range(1,21):
    bottom  = bottom * j
    
print top / bottom
