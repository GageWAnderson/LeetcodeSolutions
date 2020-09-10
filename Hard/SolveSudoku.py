#Brute-Force, instead use backtracking (DFS backtracking method)
#Complexity is O(9^(mn)) time, O(mn) space

#Need to keep this solution short to be practical for interviews, that means no extra data structures for rows,cols
class SolutionBrief:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_block_valid(i: int, j: int) -> bool:
            nums = [board[r][c] for r in range(i-2, i+1) for c in range(j-2, j+1)]
            return len(nums) == len(set(nums))

        def dfs(i: int, j: int, row: set = None) -> bool:
            if i == 9: return True
            if j == 9: return dfs(i+1, 0)
            if i % 3 == 2 and j % 3 == 2 and not is_block_valid(i, j): return False
            if j == 0: row = {str(i) for i in range(1, 10)} - set(board[i])
            if board[i][j] != '.': return dfs(i, j+1, row)
            if row:
                for num in row & cols[j]:
                    board[i][j] = num
                    cols[j].discard(num)
                    row.discard(num)
                    if dfs(i, j+1, row): return True
                    cols[j].add(num)
                    row.add(num)
                board[i][j] = '.'
            return False

        used_cols = [set(row[j] for row in board) for j in range(9)]
        cols = [{str(i) for i in range(1, 10)} - nums for nums in used_cols]
        dfs(0, 0)