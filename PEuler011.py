# Euler Problem #11: Largest product in a grid
# http://projecteuler.net/problem=11
# Q: What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# A: 70600674

# Step 1: Store data
# Save data as a .txt file via copy paste into Notepad. Import and read by line. Convert to integers and list.
# store in form of rownumber = [num1,num2...,num20]
# store all rows into one main list

f = open('p11.txt','r')
lines = f.readlines()
f.close()

data = []
for line in lines:
    row_temp = []
    for index in range(20):#20 total numbers. data in the form 'nn nn nn ...'
        row_temp += [int(line[index*3:index*3+2])]
    data += [row_temp]
    
#import stuff Debug    
#print data
#for i in range(20):
    #print data[i]
    #print len(data[i])
#end debug

# To access row i, column j, data[i][j] ; assuming indexes from 0-19
# data[6][8]*data[7][9]*data[8][10]*data[9][11] should = 26 × 63 × 78 × 14 = 1788696 by problem site
# print data[6][8]*data[7][9]*data[8][10]*data[9][11]

# Step 2: Iterate through all direction combinations, store greatest product.


# Initialize
g_prod = 0
temp_prod = 0

# Columns:
for i in range(17): # since using 4 numbers
    temp_prod = 0
    for j in range(20):
        temp_prod = data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j]
        if temp_prod > g_prod:
            g_prod = temp_prod
            #print 'updated'
# Rows:
for i in range(20): 
    temp_prod = 0
    for j in range(17):
        temp_prod = data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3]
        if temp_prod > g_prod:
            g_prod = temp_prod
            #print 'updated'
# Diagonals; down right, equivalent to up left
for i in range(17): 
    temp_prod = 0
    for j in range(17):
        temp_prod = data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3]
        if temp_prod > g_prod:
            g_prod = temp_prod
            #print 'updated'
# Diagonals; down left, equivalent to up right
for i in range(17): 
    temp_prod = 0
    for j in range(3,20):
        temp_prod = data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3]
        if temp_prod > g_prod:
            g_prod = temp_prod
            
print g_prod
