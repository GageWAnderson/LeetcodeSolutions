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

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Idea: Sliding Window since time is contiguous over the array and
        we're trying to maximize a value over that window - should make
        you jump to a dynamic sliding window solution after proposing brute-force.
        """
        if len(prices) == 1:
            return 0
        
        maxProfit = 0
        
        left,right = 0, 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            right += 1
        
        while left < len(prices):
            maxProfit = max(maxProfit, prices[right - 1] - prices[left])
            left += 1
        
        return maxProfit