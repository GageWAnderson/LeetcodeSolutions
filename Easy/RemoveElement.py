class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        numRemoved = 0
        i = 0
        while i < n - numRemoved:
            if nums[i] == val:
                lastIndex = n - numRemoved - 1
                nums[i],nums[lastIndex] = nums[lastIndex], nums[i]
                numRemoved += 1
            else:
                i += 1
        return n - numRemoved