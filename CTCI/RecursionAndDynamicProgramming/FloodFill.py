from random import randint
from collections import deque

class Board:
    """
    An m x n board where -1 represents a blocker and any other integer
    represents a color (0 represents blank).
    """
    def __init__(self, board=None, m=0, n=0, blockerDensity=0) -> None:
        if board:
            self.board = board
        else:
            self.board = self._generateRandomBoard(m, n, blockerDensity)

    def __str__(self):
        return str(self.board)
    
    def _generateRandomBoard(self, m, n, blockerDensity):
        if blockerDensity < 0 or blockerDensity > 100:
            raise Exception("Blocker density must be between 0 and 100 inclusive.")
        board = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                x = randint(0, 100)
                if x <= blockerDensity:
                    board[i][j] = -1
        return board
    
    def floodFill(self, startRow, startCol, color):
        seen = set()
        queue = deque()
        m, n = len(self.board), len(self.board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue.append((startRow, startCol))
        while queue:
            (currRow, currCol) = queue.popleft()
            seen.add((currRow, currCol))
            self.board[currRow][currCol] = color
            for dir in dirs:
                newRow, newCol = currRow + dir[0], currCol + dir[1]
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and (newRow, newCol) not in seen and self.board[newRow][newCol] != -1:
                    queue.append((newRow, newCol))

if __name__ == "__main__":
    numTests = 1
    for test in range(1, numTests + 1):
        board = Board(None, 10, 10, 50)
        board.floodFill(randint(0, len(board.board) - 1), randint(0, len(board.board[0]) - 1), 1)
        print(board)