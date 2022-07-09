class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        if n == 0:
            if target <= nums[0]:
                return 0
            else:
                return 1
            
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif mid == 0 and target < nums[mid]:
                return 0
            elif mid == n and target > nums[mid]:
                return n + 1
            elif mid != 0 and nums[mid - 1] < target and target < nums[mid]:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1