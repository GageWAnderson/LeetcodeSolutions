#Approach is left,right product lists
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        left = [0 for x in range(len(nums))]
        left[0] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        right = [0 for x in range(len(nums))] #O(n) space
        right[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
            
        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res