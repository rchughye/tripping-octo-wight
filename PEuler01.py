# Euler Problem #1: Multiples of 3 and 5
# http://projecteuler.net/problem=1
# Q: Find the sum of all the multiples of 3 or 5 below 1000.
# A: 233168

# Closed form solution:
# Sum the arithemetic series of multiples of 3 and 5, then subtract the arithmetic series of 15 to avoid double counting
# Based off formula s = n(a1 + an)/2
# 333 multiples of 3 less than 1000
# 199 multiples of 5 less than 1000
# 66 multiples of 15 less than 1000

m3 = 333 * (3 + 999) / 2
m5 = 199 * (5 + 995) / 2
m15 = 66 * (15 + 990) / 2

print m3 + m5 - m15

# Computer Summing
# produce lists of multiples of 3,5,15 then iteratively add and subtract appropriate elements

c3 = range(3,1000,3)
c5 = range(5,1000,5)
c15 = range(15,1000,15)
sum_total = 0

for i in c3:
    sum_total += i
for i in c5:
    sum_total += i
for i in c15:
    sum_total = sum_total - i

print sum_total
