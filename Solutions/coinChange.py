"""
Got the approach right, however missed the desired behavior on an edge case.
Read and TAKE NOTES on the problem statement before actually coding.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if not coins:
            return -1
        
        dp = [None for _ in range(amount)]

        for coin in coins:
            if coin <= amount:
                dp[coin - 1] = 1
        
        for i in range(amount):
            if dp[i] == 1:
                continue
            
            prev = []
            for coin in coins:
                if (i - coin) >= 0 and dp[i - coin]:
                    prev.append(dp[i - coin])
            if prev:
                dp[i] = min(prev) + 1
        
        return dp[-1] if dp[-1] and (dp[-1] > 0) else -1