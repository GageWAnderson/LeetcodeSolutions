from collections import deque
#Can be done in O(mn) space non-destructively
class Solution: #Almost got this right first try
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        m,n = len(grid),len(grid[0])
        if n == 0: return 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    maxA = max(maxA,self.bfs(row,col,grid))
                    print(f"maxA = {maxA}")
        return maxA
    
    def bfs(self,x,y,grid):
        q = deque()
        area = 0
        q.append((x,y))
        grid[x][y] = 0 #Mark start as seen
        while q:
            node = q.popleft()
            area += 1
            for nbor in self.getNbors(node,grid):
                grid[nbor[0]][nbor[1]] = 0 #Destructive BFS, need to mark nbor as seen as soon as it is appended
                q.append(nbor)
                
        return area
            
    def getNbors(self,node,grid):
        x,y = node
        m,n = len(grid),len(grid[0])
        dirs = [(0,-1),(0,1),(-1,0),(1,0)] #Up,down,left,right
        res = []
        
        for move in dirs:
            newX = x + move[0]
            newY = y + move[1]
            if newX >= 0 and newY >= 0 and newX < m and newY < n and grid[newX][newY] == 1:
                res.append((newX,newY))
        return res