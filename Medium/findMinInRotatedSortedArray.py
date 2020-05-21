#I improves a lot at binary search, I wrote some pretty clean code here!
#However, I was already pretty familiar with the problem, hope I can apply this to arrays in the future!
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] #Clean up the input
        lower,upper = 0,len(nums)-1
        if nums[lower] < nums[upper]: return nums[lower] #Chekc if the input is already sorted
        
        while (upper - lower) > 1:
            mdpt = lower + (upper - lower)//2
            if(nums[mdpt] < nums[upper]): upper = mdpt
            else: lower = mdpt
        return nums[lower + 1]