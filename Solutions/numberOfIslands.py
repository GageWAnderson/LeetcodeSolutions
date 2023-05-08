from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        res = 0

        def getNbors(row, col):
            nbors = []
            if row > 0 and grid[row - 1][col] == "1":
                nbors.append((row - 1, col))
            if col > 0 and grid[row][col - 1] == "1":
                nbors.append((row, col - 1))
            if row < m - 1 and grid[row + 1][col] == "1":
                nbors.append((row + 1, col))
            if col < n - 1 and grid[row][col + 1] == "1":
                nbors.append((row, col + 1))
            return nbors

        def bfs(row, col):
            queue = deque() # O(min(m, n)) space, BFS is space-optimal

            queue.append((row, col))
            while queue:
                currRow, currCol = queue.popleft()
                grid[currRow][currCol] = "0"
                for nbor in getNbors(currRow, currCol):
                    queue.append((nbor[0], nbor[1]))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    res += 1
                    bfs(row, col)
        return res