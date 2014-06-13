# Euler Problem #24: Lexicographic permutations
# http://projecteuler.net/problem=24
# Q: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# A: 2783915460

# represent as string, use built in permutations function to find permutations

# initialize
counter = 1
output = ''

import itertools
for i in itertools.permutations("0123456789"):
    if counter == 1000000:
        for l in i:
            output += l
        print output
    counter +=1
