#CTCI 1.8, use two hash sets seen (rows,cols) to keep track of what rows,cols are set to 0

#You do not need to check O(mn) elements, because some of them will be 0 garunteed
#You keep track of this with these hash sets so you don't need to look at everything

def setToZero(matrix,zeroRows,zeroCols,m,n): #O(mn)
    for row in range(m):
        for col in range(n):
            if row in zeroRows or col in zeroCols:
                matrix[row][col] = 0
    return matrix
    

#This is buggy, need to continue looking at a row even after I find 0, then set
#The entire row to 0 after setting the required columns to 0

#You need to set everything to 0 at the end otherwise you lose the information on where the
#zeros are located (this forces O(mn))
def zeroMatrix(matrix):
    m,n = len(matrix),len(matrix[0])
    zeroRows = set()
    zeroCols = set()

    for row in range(m): #O(mn)
        for col in range(n):
            if matrix[row][col] == 0:
                zeroRows.add(row)
                zeroCols.add(col)
    return setToZero(matrix,zeroRows,zeroCols,m,n)
                
if __name__ == "__main__":
    matrix = [[1,1,0,19]*4,[1,1,1,1]*4]
    print(matrix)
    zeros = zeroMatrix(matrix)
    print(zeros)