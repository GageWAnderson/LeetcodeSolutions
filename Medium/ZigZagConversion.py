class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1): return s
        
        rowNum = min(numRows,len(s))
        rowStrings = [""] * rowNum
        goingDown = False #keep track of what direction you are headed
        #Insight here is to use a variable to keep track of what direction
        #You are headed in!
        
        row = 0
        for i in range(len(s)): #loop through all the characters in s (NOT len(s) -1)
            if(row == 0 or row == numRows-1):
                goingDown = not goingDown
            rowStrings[row] += s[i]
            if(goingDown):
                row += 1
            else:
                row -= 1
        
        ans = ""
        for rowString in rowStrings: #make the answer from the rows
            ans += rowString
        return ans

#I had a lot of trouble seeing the pattern here
#I missed the key insight to track which direction you are going
#With the goingDown variable 
#Then adding to and reading the rows line by line