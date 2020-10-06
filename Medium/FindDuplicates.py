class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return []
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            nums[abs(num)-1] *= -1
        
        return res