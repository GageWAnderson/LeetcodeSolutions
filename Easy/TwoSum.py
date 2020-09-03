class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1: return []
        seen = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]] = i
        return []