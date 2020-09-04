#Find the number of ways to make the change with 1 coin, then the second, then the third...
#This problem has an optimal substructure property -> Means DP (optimal solution from optimal sub-problem sol'ns)
class SolutionOptimal: #Uses O(1) space to store DP results
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for x in range(amount+1)] #Use O(n) space here
        dp[0] = 0 #1 way to make 0 cents with no coins
        for coin in coins:
            for i in range(coin,len(dp)):
                dp[i] = min(dp[i], dp[i-coin]+1) #This is the key line
        return dp[-1] if dp[-1] != inf else -1