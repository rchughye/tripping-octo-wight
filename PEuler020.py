# Euler Problem #20: Factorial digit sum
# http://projecteuler.net/problem=20
# Q: Find the sum of the digits in the number 100!
# A: 648

# Store number then sum digits
# Initialize
n = 1
total = 0

for i in range(1,101):
    n = n * i

s = str(n)

# Sum digits
for index in range(len(s)):
    total += int(s[index])
    
print total
