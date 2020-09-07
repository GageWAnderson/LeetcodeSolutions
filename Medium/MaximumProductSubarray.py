#DP solution for O(n^2) -> may be able to optimize this to O(n)
class SolutionSlow: #Brute force, just try all the contiguous intervals
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        dp = nums[::] #Remember to make this a deep copy
        res = -inf
        for j in range(1,len(nums)):
            product = 1
            for i in range(j):
                product *= nums[i]
                if product > res:
                    res = product
        
        for i in range(len(nums)):
            product = 1
            for j in range(i,len(nums)):
                product *= nums[j]
                if product > res:
                    res = product
        
        return res

#Should be able to get an O(n) solution with some clever DP...

#I forgot to consider 0 in my first attempt at an O(n) solution
#Keeping track of the max,min as you got lets you handle negative numbers
class SolutionBest: #Not DP...
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        res = nums[0]
        
        for i in range(1,len(nums)):
            curr = nums[i]
            tmp = max(curr,max_so_far*curr,min_so_far*curr)
            min_so_far = min(curr,max_so_far*curr,min_so_far*curr)
            max_so_far = tmp
            
            res = max(res,max_so_far)
        
        return res

# But this solution show us a new way: Our dp array can store more data than just a single value. 
# The reason why the above solution does not use the dp array is that dp[i] only depends on dp[i - 1] so there 
# is no need to save all the previous max and min data, just save the previous max and min value(dp[i - 1]).