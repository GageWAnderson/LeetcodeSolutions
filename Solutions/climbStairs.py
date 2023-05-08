class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        prev2, prev1 = 1,2
        curr = None
        for i in range(2, n):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr