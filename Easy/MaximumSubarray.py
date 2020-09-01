#I overthought this question quite a lot...
#Also, trying all the contiguous windows is simply O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currSum,maxSum = nums[0],nums[0]
        
        for i in range(1,n):
            currSum = max(nums[i],currSum+nums[i])
            maxSum = max(maxSum,currSum)
        
        return maxSum