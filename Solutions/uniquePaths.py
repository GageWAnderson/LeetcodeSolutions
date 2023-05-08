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