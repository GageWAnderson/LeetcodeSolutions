class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        
        return False