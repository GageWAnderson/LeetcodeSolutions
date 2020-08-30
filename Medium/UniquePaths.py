class Solution: #This was really easy
    def uniquePaths(self, m: int, n: int) -> int: #O(mn) time and space
        if m == 0 or n == 0: return 1 #m == cols, n == rows
        dp = [[-1 for x in range(m)] for y in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    dp[i][j] = 1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]