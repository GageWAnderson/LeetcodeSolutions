#Distinct ways -> DP (permutations, not combonations)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 1
        dp = [0 for x in range(n+1)] #Remember to account for n=0
        dp[0] = 1 #DP includes the 0th step
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]