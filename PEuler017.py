# Euler Problem #17: Number letter counts
# http://projecteuler.net/problem=17
# Q: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
# A: 21124

# Parse separate categories: 1-19, 20-99, 100-999, 1000, sum totals at end

# Initialize
total = 0

# Make a dictionary for general usage
# num -> # of letters
d = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,0:0}
d[10] = 3
d[11] = len('eleven')
d[12] = len('twelve')
d[13] = len('thirteen')
d[14] = len('fourteen')
d[15] = len('fifteen')
d[16] = len('sixteen')
d[17] = len('seventeen')
d[18] = len('eighteen')
d[19] = len('nineteen')
d[20] = len('twenty')
d[30] = len('thirty')
d[40] = len('forty')
d[50] = len('fifty')
d[60] = len('sixty')
d[70] = len('seventy')
d[80] = len('eighty')
d[90] = len('ninety')
d['hundred'] = 7
d['and'] = 3

# 1-19:
# Since hard coded:
for i in range(1,20):
    total += d[i]
#print total

# 20-99:
# Composed of tens digit name and ones digit name
for i in range(2,10):
    for j in range(10):
        total += d[i*10] + d[j]

# 100-999:
# Composed of hundred digit name, and 'hundred and' and remaining digit
# Exceptions: 100,200,...,900

# x00
for i in range(1,10):
    total += d[i] + d['hundred']

# x01-x19, excluding x00
for i in range(1,10):
    for j in range(1,20):
        total += d[i] + d['hundred'] + d['and'] + d[j]

# x20- x99
# in form of 'x hundred and 10 digit 1 digit'
for i in range(1,10):
    for j in range(20,91,10):
        for k in range(10):
            total+= d[i] + d['hundred'] + d['and'] + d[j] + d[k]


# 1000
total += d[1] + len('thousand')

print total
