class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        best = 0
        l,r = 0,1

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                best = max(best, prices[r] - prices[l])
                r += 1
        
        return best