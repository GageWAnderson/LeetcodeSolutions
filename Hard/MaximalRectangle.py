#Brute force is O(n^4), have to look at the whole board every matrix entry
#Need to keep track of the squares I have looked at already

#Best solution to this problem Uses the max histogram algorithm on every row of the matrix
#This solution is genius...
class Solution: #O(n^2), assuming the matrix is square otherwise O(mn)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #rows,cols = len(matrix),len(matrix[0]) Don't declare these at the same time since cols can index out of range on empty matrix
        rows = len(matrix)
        if rows == 0: return 0
        cols = len(matrix[0])
        self.convertToInts(matrix) #O(n^2), for convenience
        res = 0
        for i in range(rows): #O(n)
            if i != 0:
                self.updateRow(matrix[i],matrix[i-1]) #Extend the histogram row by row
            print(matrix[i])
            res = max(res,self.largestRectangleArea(matrix[i])) #O(n)
            print(f"res = {res}")
        return res
            
    def updateRow(self,currRow,aboveRow):
        for j in range(len(currRow)):
            if aboveRow[j] != 0 and currRow[j] != 0:
                currRow[j] += aboveRow[j]
                    
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        posStack = []
        heights.append(0)
        for i,h in enumerate(heights):
            while posStack and heights[posStack[-1]] > h:
                currHeightPos = posStack.pop()
                start = posStack[-1] + 1 if posStack else 0
                end = i - 1
                width = end - start + 1
                res = max(res, width*heights[currHeightPos])
            posStack.append(i)
        return res
    
    def convertToInts(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == "0"):
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1