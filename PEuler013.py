# Euler Problem #13: Large sum
# http://projecteuler.net/problem=13
# Q: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# A: 5537376230

# To find the first 10 digits of the sum, one only needs to consider 11 digits
# since 10^8, the lowest possible 8 digits number, repeated 100 times is 10^10, which is 10 digits.
# Then since there are 100 numbers, 3 more digits must be considered as the remaining total affects the final digits
# consider additional digit in case of misunderstanding

# Step 1: Import in numbers
# Save data as a .txt file via copy paste into Notepad. Import and read by line. Convert to integers.


f = open('p13.txt','r')
lines = f.readlines()
f.close()

# Step 2: Add numbers while converting to integers.

total = 0
for line in lines:
    total += int(line[:12]) # 12 digits as discussed above
    
print str(total)[:10]
