#Ok so graph algorithms are way overthinking this problem...
#The optimal solution is Greed and can get O(1) space!
class SolutionDP: #O(n^2), this was pretty slow and really easy
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        dp = [inf for x in range(n)] #Need to make sure distances are originally set to inf
        dp[-1] = 0
        dp[-2] = 1
        
        for i in range(n-2,-1,-1):
            if n - i < nums[i]: #Made a dumb mistake here...
                dp[i] = 1
            else:
                dp[i] = min(dp[i:i+nums[i]+1]) + 1
        return dp[0]