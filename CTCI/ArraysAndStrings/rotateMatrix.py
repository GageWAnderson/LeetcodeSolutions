#CTCI 1.7, rotate image by 90 degrees (like the 15-122 homework!)
#In order to do this in place you need to use swap to not allocate more space

def swap(matrix,startRow,startCol,endRow,endCol):
    tmp = matrix[startRow][startCol]
    matrix[startRow][startCol] = matrix[endRow][endCol]
    matrix[endRow][endCol] = tmp

def rotateX(matrix,N):
    for row in range(N//2):
        for col in range(N):
            swap(matrix,row,col,(N-1)-row,col)

def rotateY(matrix,N):
    for row in range(N):
        for col in range(N//2):
            swap(matrix,row,col,row,(N-1)-col)

def rotateMatrix(matrix): #Rotates 90 degrees
    N = len(matrix) #NxN matrix
    rotateX(matrix,N)
    rotateY(matrix,N)
    rotateX(matrix,N)
    return matrix