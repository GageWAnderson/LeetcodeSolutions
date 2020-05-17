def isValid(row,col,width,height):
    return (row >= 0 and row < height and col >= 0 and col < width)

def dfs(board,row,col):
    dirs = [(-1,0),(1,0),(0,-1),(0,1)] #up,down,left,right
    
    numRows = len(board)
    numCols = len(board[0]) #Assumes the board is square
    if(board[row][col] == '0'): return
    else:
        board[row][col] = '0'
        for dir in dirs:
            (newR,newC) = (row + dir[0], col + dir[1])
            if(isValid(newR,newC,numCols,numRows) and board[newR][newC] != '0'): #numRows is the height not the width!
                print(f"newR = {newR}, newC = {newC}")
                dfs(board,newR,newC)
    
class Solution: #O(n), however uses naive DFS and is destructive of the islands- this question can get way more interesting and could
    #require and implementation of Jarnik-Primm's or Kruskal's with Union-Finds (w/ height tracking and path-compression)
    def numIslands(self, grid: List[List[str]]) -> int: #Note that each element of the grid is a string, not an int, so you need to convert to int!
        (row,col) = (0,0)
        numRows = len(grid)
        if(numRows == 0): return 0 #Need to account for edge cases in the input!!!
        numCols = len(grid[0]) #Assumes the board is square
        numIslands = 0
        
        for row in range(numRows):
            for col in range(numCols):
                if(grid[row][col] == '0'): continue
                else:
                    dfs(grid,row,col)
                    numIslands += 1
        
        return numIslands #Make sure to return at the end!