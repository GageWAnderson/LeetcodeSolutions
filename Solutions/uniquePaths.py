class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [[1 for _ in range(min(m,n))]]
        dp.append([0 for _ in range(min(m,n))])
        dp[1][0] = 1

        for row in range(1, max(m,n)):
            for col in range(1, min(m,n)):
                dp[1][col] = dp[0][col] + dp[1][col - 1]
        
            dp[0] = copy.deepcopy(dp[1])
            dp[1] = [0 for _ in range(min(m,n))]
            dp[1][0] = 1
        
        print(dp)
        return dp[0][-1]

import copy
class SolutionMemoryOptimized:
    def uniquePaths(self, m: int, n: int) -> int:
        # Set m to be smaller than n
        if m > n:
            m,n = n,m

        prev_row = [1 for col in range(m)] # O(min(m,n)) memory
        curr_row = [1 if col == 0 else 0 for col in range(m)]
        for row in range(1, n):
            for col in range(1, m):
                curr_row[col] = curr_row[col - 1] + prev_row[col]
            prev_row = copy.deepcopy(curr_row)
            curr_row[0] = 1
        return curr_row[-1]