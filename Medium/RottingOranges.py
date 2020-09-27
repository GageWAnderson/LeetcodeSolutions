class Solution: #BFS with multiple start points
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_oranges = 0
        num_rotten = 0
        m,n = len(grid),len(grid[0])
        moves = [(0,-1),(0,1),(-1,0),(1,0)]
        rotten_start = []
        
        def isSafe(x,y):
            return x >= 0 and y >= 0 and x < m and y < n
        
        def getNbors(node):
            nbors = []
            x,y,t = node
            for move in moves:
                if isSafe(x+move[0],y+move[1]):
                    nbors.append((x+move[0],y+move[1]))
            return nbors
        
        #First, get the total number of oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    num_oranges += 1
                if grid[i][j] == 2:
                    rotten_start.append((i,j,0))
                    num_rotten += 1
                    
        if num_rotten >= num_oranges:
            return 0
                    
        q = deque(rotten_start) #x=0,y=0,mins=0
        #print(f"num_oranges = {num_oranges}")
        #print(f"num_rotten = {num_rotten}")
        while q:
            #print(q)
            curr = q.popleft()
            x,y,t = curr
            
            if num_rotten >= num_oranges: #End when all rotten
                if q:
                    return max(q,key = lambda x : x[2])[2]
                else:
                    return t
            
            if grid[x][y] == 2:
                for nbor in getNbors(curr):
                    if grid[nbor[0]][nbor[1]] == 1:
                        grid[nbor[0]][nbor[1]] = 2 #Spread rot
                        num_rotten += 1
                        q.append((nbor[0],nbor[1],t+1))
                    
        return -1

#Note: When multiple start points are required, just add them all to the queue!