class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        seen[nums[0]] = 0

        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        
        return None