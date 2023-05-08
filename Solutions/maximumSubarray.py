class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        currSum = 0
        maxSum = None
        l,r = 0,0
        
        while r < len(nums):
            currSum += nums[r]
            maxSum = max(maxSum, currSum) if (maxSum is not None) else currSum
            r += 1
            if currSum < 0:
                l = r
                currSum = 0
        
        while l < len(nums):
            maxSum = max(currSum, maxSum)
            currSum -= nums[l]
            l += 1
        
        return maxSum