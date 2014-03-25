# Euler Problem #22: Names scores
# http://projecteuler.net/problem=22
# Q: What is the total of all the name scores in the file?
# A: 871198282

# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# Import list, sort into alphabetical order, iterate over all elements and sum scores

# Import
f = open('p22.txt','r')
lines = f.readlines()
f.close()

# Initialize
l = []
total = 0

# Sort
l = lines[0].split(",")
l.sort()

# Iterate and sum scores using index of list as it's alphabetical position
# note, names are in the form "name" with quotation marks. need to strip them
# Use the ord function minus 64 to get alphabetical value of letters
# ord("A") -> 65

for i in range(len(l)):
    name = l[i].strip('"')
    temp = 0
    for let in name:
        temp += ord(let) - 64
    total += temp * (i + 1)

print total
