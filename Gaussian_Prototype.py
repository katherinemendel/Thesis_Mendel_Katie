import numpy as np

numRows = 4
numCols = 4

matrix = np.random.rand(4, 4)

print(matrix)

#Complexity

#For n < numRows in matrix
for n in range(numRows-1):
    pivot_term = matrix[n,n]

    #TODO deal with 0 case

    #flip flop rows down??
    matrix[n,] = matrix[n,]/pivot_term

    factor = matrix[n+1,n]

    matrix[n+1,] = matrix[n+1,] - (factor * matrix[n,])

    for i in range(numRows-n):
        print(i) 
        matrix[n+1,] =  matrix[i+n,] *  matrix[n+1,]

matrix[numRows-1,] = matrix[numRows-1,]/matrix[numRows-1,numRows-1]
print(matrix)