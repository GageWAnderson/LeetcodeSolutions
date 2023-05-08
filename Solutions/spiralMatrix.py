class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        seen = set()

        def getNewDirection(row, col, direction):
            newDirection = direction
            if direction == (0,1) and (col == COLS - 1 or (row, col + 1) in seen):
                newDirection = (1,0) # Right to Down
            elif direction == (1,0) and (row == ROWS - 1 or (row + 1, col) in seen):
                newDirection = (0, -1) # Down to left
            elif direction == (0, -1) and (col == 0 or (row, col - 1) in seen):
                newDirection = (-1, 0) # Left to up
            elif direction == (-1, 0) and (row == 0 or (row - 1, col) in seen):
                newDirection = (0, 1) # Up to Right

            # Otherwise the new direction is simply the old direction
            return newDirection
        
        def getNbors(row, col, direction):
            nbors = []
            newRow, newCol = row + direction[0], col + direction[1]
            if newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS:
                nbors.append((row + direction[0], col + direction[1]))
            return nbors

        def dfs(row, col, direction):
            if (row, col) in seen:
                return
            
            res.append(matrix[row][col])
            seen.add((row, col))
            newDirection = getNewDirection(row, col, direction)
            for nbor in getNbors(row, col, newDirection):
                dfs(nbor[0], nbor[1], newDirection)
        
        dfs(0, 0, (0, 1))
        return res