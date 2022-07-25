class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        
        def dfs(row, col, wordSoFar):
            wordSoFar.append(board[row][col])
            if len(wordSoFar) == len(word):
                if word[-1] == wordSoFar[-1]:
                    return True
                else:
                    wordSoFar.pop()
                    return False
            elif wordSoFar[-1] != word[len(wordSoFar) - 1]:
                wordSoFar.pop()
                return False
            else:
                visited.add((row,col))
                for move in moves:
                    newRow, newCol = row + move[0], col + move[1]
                    if newRow >= 0 and newRow < m and newCol >=0 and newCol < n:
                        if (newRow, newCol) not in visited and dfs(newRow, newCol, wordSoFar):
                            return True
                visited.remove((row,col))
                wordSoFar.pop()
                return False
        
        for startRow in range(m):
            for startCol in range(n):
                if dfs(startRow, startCol, []):
                    return True
                visited.clear()
        return False