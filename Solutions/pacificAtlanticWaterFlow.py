class SolutionSlow:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        canReach = [[[False, False] for _ in range(n)] for _ in range(m)]
        seen = set()

        def getNbors(row, col):
            nbors = []
            currHeight = heights[row][col]
            if row > 0 and heights[row - 1][col] <= currHeight:
                nbors.append((row - 1, col))
            if col > 0 and heights[row][col - 1] <= currHeight:
                nbors.append((row, col - 1))
            if row < m - 1 and heights[row + 1][col] <= currHeight:
                nbors.append((row + 1, col))
            if col < n - 1 and heights[row][col + 1] <= currHeight:
                nbors.append((row, col + 1))
            return nbors

        def dfs(row, col, prev):
            if row == 0 or col == 0 or canReach[row][col][0]:
                canReach[row][col][0] = True # Can reach Pacific Ocean
                for prevRow,prevCol in prev:
                    if not canReach[prevRow][prevCol][0]:
                        canReach[prevRow][prevCol][0] = True # Cascade result upstream
                    else:
                        break
            if row == m - 1 or col == n - 1 or canReach[row][col][1]:
                canReach[row][col][1] = True
                for prevRow,prevCol in prev:
                    if not canReach[prevRow][prevCol][1]:
                        canReach[prevRow][prevCol][1] = True
                    else:
                        break
            
            if canReach[row][col][0] and canReach[row][col][1]:
                return # Terminate search if you can reach both
            
            seen.add((row, col))
            for nborRow,nborCol in getNbors(row,col):
                if (nborRow, nborCol) not in seen:
                    prev.append((row, col))
                    dfs(nborRow, nborCol, prev)
                    prev.pop()
            seen.remove((row, col))
        
        for row in range(m):
            for col in range(n):
                dfs(row, col, [])
        
        res = []
        for r in range(m):
            for c in range(n):
                if canReach[r][c][0] and canReach[r][c][1]:
                    res.append([r,c])
        return res

class SolutionOptimal:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def getNbors(row, col, prevHeight):
            nbors = []
            if row > 0 and heights[row - 1][col] >= prevHeight:
                nbors.append((row - 1, col))
            if col > 0 and heights[row][col - 1] >= prevHeight:
                nbors.append((row, col - 1))
            if row < ROWS - 1 and heights[row + 1][col] >= prevHeight:
                nbors.append((row + 1, col))
            if col < COLS - 1 and heights[row][col + 1] >= prevHeight:
                nbors.append((row, col + 1))
            return nbors

        def dfs(row, col, seen):
            seen.add((row, col))
            for nborRow,nborCol in getNbors(row, col, heights[row][col]):
                if (nborRow, nborCol) not in seen:
                    dfs(nborRow, nborCol, seen)
        
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res