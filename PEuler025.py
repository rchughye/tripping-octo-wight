# Euler Problem #25: 1000-digit Fibonacci number
# http://projecteuler.net/problem=25
# Q: What is the first term in the Fibonacci sequence to contain 1000 digits?
# A: 4782

# Initialize
F_old = 1
F_new = 1
temp = 1
counter = 2

while F_new <= 10 ** 999:
    temp = F_new
    F_new += F_old
    F_old = temp
    counter += 1

print counter
