# Euler Problem #14: Longest Collatz sequence
# http://projecteuler.net/problem=14
# Q: Which starting number, under one million, produces the longest chain?
# A: 837799

# Try to test all Collatz sequences up to 999 999 (Very slow)

# Initialize; use while loop iteration to avoid creation of million element list (not sure if relevant)
longest_chain = 0
longest = 0
loop = 1


while loop != 999999:
    temp = loop
    counter = 0
    while temp != 1:
        if temp%2 == 0 : # if even
            temp = temp/2
        else:
            temp = 3 * temp + 1
        counter += 1
    if counter > longest_chain:
        longest_chain = counter
        longest = loop
    loop += 1
    
print longest
