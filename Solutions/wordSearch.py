class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        seen = set()

        def getNbors(row, col):
            res = []
            if row > 0 :
                res.append((row - 1, col))
            if row < m - 1:
                res.append((row + 1, col))
            if col > 0:
                res.append((row, col - 1))
            if col < n - 1:
                res.append((row, col + 1))
            return res

        def dfs(currWordIndex, currRow, currCol):
            if currWordIndex == len(word) - 1 and board[currRow][currCol] == word[currWordIndex]:
                return True
            
            if word[currWordIndex] != board[currRow][currCol]:
                return False
            
            seen.add((currRow, currCol))
            for nbor in getNbors(currRow, currCol):
                nborRow, nborCol = nbor[0], nbor[1]
                if nbor not in seen and dfs(currWordIndex + 1, nborRow, nborCol):
                    return True

            seen.remove((currRow, currCol))
            return False
            
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True

        return False