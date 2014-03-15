# Euler Problem #67: Maximum path sum II
# http://projecteuler.net/problem=67
# Q: Find the maximum total from top to bottom
# A: 7273

# Copy algorithm from problem 18

# Iterate down the triangle, storing the maximum sum of all paths for each node of the triangle
# each maximum sum is the max of the connected prior maxmimum plus the current node value

# Store the triangle in an ixj matrix.

f = open('p67.txt','r')
lines = f.readlines()
f.close()

data = []

for line in lines:
    temp = []
    for n in line.split():
        temp += [int(n)]
    data += [temp]

# data[i][j] produces the i row and jth number from the left. Note: 0 based index
# data[3][2] -> 6

# Iterate down the triangle, storing a row of max sums. At end, output max of row of max sums.
# Could alternatively store another matrix of max sums for each node, would take more memory
# Initialize

max_row = [59]
temp_row = [59] # placeholder for holding the prior row of max sums


# data[i][j] is connected to data[i-1][j-1] and data[i-1][j]
# must also deal with end cases such that  0 >= j >= i

for i in range(1,len(data)):
    for j in range(i+1):
        #End case 1: j = 0, leftmost node, only 1 path leads to this node
        if j == 0:
            max_row[j] = data[i][j] + temp_row[j]
        #End case 2: last element of row. only 1 path leads to this node
        elif j == i:
            max_row.append(data[i][j] + temp_row[j-1])
        #add the value of the node to the max of the prior two connected nodes
        else:
            max_row[j] = data[i][j] + max(temp_row[j-1],temp_row[j])
            
    for k in range(len(max_row)):#update temp_row values; watch for issues with copying pointer to list
        if k == len(max_row)-1:
            temp_row.append(max_row[k])
        else:
            temp_row[k] = max_row[k]

print max(max_row)
