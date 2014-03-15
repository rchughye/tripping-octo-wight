# Euler Problem #16: Power digit sum
# http://projecteuler.net/problem=16
# Q: What is the sum of the digits of the number 2^1000?
# A: 1366

# Store as string, sum digits

# Initialize
n = str(2**1000)
total = 0

# Sum digits
for index in range(len(n)):
    total += int(n[index])

print total
    
