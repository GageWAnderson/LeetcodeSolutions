class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = []
        board = [["." for row in range(n)] for col in range(n)]
        
        # Tracks if a queen is present in a given col, diag or anti-diag
        cols, diags, antiDiags = set(), set(), set()
        
        def isSafe(row, col):
            if col in cols:
                return False
            if (row - col) in diags:
                return False
            if (row + col) in antiDiags:
                return False
            return True
        
        def flatten(board):
            res = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(board[i][j])
                row = "".join(row)
                res.append(row)
            return res
        
        def placeQueen(board, row):
            if row == n:
                solution.append(flatten(board))
            else:
                for col in range(n):
                    if isSafe(row, col):
                        board[row][col] = "Q"
                        cols.add(col)
                        diags.add(row - col)
                        antiDiags.add(row + col)
                        
                        placeQueen(board, row + 1)
                        
                        board[row][col] = "."
                        cols.remove(col)
                        diags.remove(row - col)
                        antiDiags.remove(row + col)
        
        placeQueen(board, 0)
        return solution