class Solution:
    """
    Can go faster by building result from the ground up.
    Don't need to re-construct the number every time.
    Provides a CONSTANT-TIME speedup - look for this in bit shifting problems.
    O(nlogn) -> Perform at most logn operations per number
    """
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            numOnes = 0
            num = i
            while num > 0:
                if (num & 1) == 1:
                    numOnes += 1
                num = num >> 1
            res.append(numOnes)
        return res

class SolutionOptimal:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            # Most significant bit plus answer for less sig. bits we've already computed
            dp[i] = 1 + dp[i - offset]
        
        return dp