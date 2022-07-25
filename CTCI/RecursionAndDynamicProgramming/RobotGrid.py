from random import randint


class Grid:

    """
    Declares a numRows x numCols grid with blockerDensity/100 % of the squares blocked.
    If no arguments are provided, generates a random grid.
    The grid is a 2D-Array of ints where 0 represents open and -1 represents blocked
    """

    def __init__(self, grid=None, numRows=10, numCols=10, blockerDensity=10) -> None:
        if not grid:
            self.grid = self._getRandomGrid(numRows, numCols, blockerDensity)
            self.numRows = numRows
            self.numCols = numCols
        else:
            self.grid = grid
            self.numRows = len(grid)
            self.numCols = len(grid[0])

    def findPathTopLeftToBottomRight(self):
        path = []
        failedPoints = set()
        targetRow, targetCol = self.numRows - 1, self.numCols - 1

        def isBlocked(row, col):
            return self.grid[row][col] == -1

        def dfs(currRow, currCol):
            if currRow < 0 or currRow > targetRow or currCol < 0 or currCol > targetCol:
                return False
            elif currRow == targetRow and currCol == targetCol:
                path.append((currRow, currCol))
                return True
            elif (currRow, currCol) in failedPoints or isBlocked(currRow, currCol):
                return False
            else:
                path.append((currRow, currCol))
                if dfs(currRow + 1, currCol):
                    return True
                elif dfs(currRow, currCol + 1):
                    return True
                else:
                    path.pop()
                    failedPoints.add((currRow, currCol))
                    return False
        
        dfs(0, 0)
        return path

    def _getRandomGrid(self, r, c, blockerDensity):
        grid = [[0 for j in range(c)] for i in range(r)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if randint(0,100) <= blockerDensity:
                    grid[i][j] = -1

        return grid

    def __str__(self) -> str:
        return str(self.grid)

if __name__ == "__main__":
    numTests = 10
    for test in range(numTests):
        grid = Grid()
        print(grid.findPathTopLeftToBottomRight())
    
    density = 30
    print(f"Trying higher blocker density = {density}")
    for test in range(numTests):
        grid = Grid(None, 50, 50, density)
        print(grid.findPathTopLeftToBottomRight())
