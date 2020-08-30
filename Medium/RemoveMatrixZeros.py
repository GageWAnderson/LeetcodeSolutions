class Solution: #Easy solution, O(mn) time, O(m + n) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        removeRows = set()
        removeCols = set()
        m,n = len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    removeRows.add(i)
                    removeCols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in removeRows or j in removeCols:
                    matrix[i][j] = 0

#Wasn't able to get the Constant space solution
#Use the first cell in each row/col to record whether or not to set it to 0
#Need to use 1 additional variable for the first row/col since matrix[0][0] represents both
class SolutionConstantSpace:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstColZero = False #First column shares a marker with the first row
        #So need a var to track whether to zero the first column
        
        m,n = len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j == 0:
                        firstColZero = True
                        matrix[i][0] = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        print(matrix)
        #Need to consider 0th row, 0th col last to preserve set zeros
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0