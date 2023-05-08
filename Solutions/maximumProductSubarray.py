class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        currMax,currMin = 1,1

        for num in nums:
            if num == 0:
                currMax,currMin = 1,1
                res = max(0, res)
            else:
                tmp = currMax
                currMax = max(num, currMax*num, currMin*num)
                currMin = min(num, tmp*num, currMin*num)
                res = max(num, res, currMax)
        
        return res