"""
Over-invested on a Greedy solution, should have aborted that when
I realized there is no optimal substructure - I need to try both
possibilities for each house. Memoization is a must for this problem,
don't rely on @lru_cache.

There is an optimal solution that is iterative - can reduce space complexity.
robFrom(i) = max(robFrom(i-2) + nums[i], robFrom(i-1))
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = dict()

        def robHelper(nums):
            if (tuple(nums)) in memo:
                return memo[tuple(nums)]
            elif not nums:
                res = 0
            elif len(nums) == 1:
                res = nums[0]
            elif len(nums) == 2:
                res = max(nums[0], nums[1])
            else:
                res = max((nums[0] + robHelper(nums[2:])), robHelper(nums[1:]))
            
            memo[tuple(nums)] = res
            return res
        
        return robHelper(nums)