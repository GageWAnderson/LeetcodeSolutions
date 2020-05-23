#CTCI 1.7, rotate image by 90 degrees (like the 15-122 homework!)
#In order to do this in place you need to use swap to not allocate more space

#This is the wrong solution!:
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

#Right solution, proceed in layers progressing towards the middle

#Solution notes:
#Do this in O(1) space like so:

# for i in range(n):
#     temp = top[i]
#     top[i] = left[i]
#     left[i] = bottom[i]
#     bottom[i] = right[i]
#     right[i] = temp

#General approach: follow 1 square, see where it needs to go in the final product
#Then figure out how to generalize this to many squares

#NOTE O(N^2) is the best we can do since we have to touch all N^2 

def rotateNotWrong(matrix):
    #Clean up the input, need an NxN matrix of nonzero size
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False 
    n = len(matrix)

    for layer in range(n//2):
        first,last = layer, n-layer-1
        for i in range(first,last):
            offset = i - first
            temp = matrix[first][i]

            #Left -> top
            matrix[first][i] = matrix[last-offset][first]

            #Bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            #Right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            #Top -> right
            matrix[i][last] = temp
    return True

#Hard part: Figuring out how to index into matrix for each swap
#Resolve this: Draw out an example, figure out the relationship for
#Each one of the 4 swaps made!