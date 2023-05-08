"""
Got the right approach quickly after looking at the problem, but I didn't consider the case
of looking at the midpoint before discluding it from the problem space.
The implementation was much harder than figuring out the approach. This will improve with practice.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2
            low,mid,high = nums[l],nums[m],nums[r]

            # First, check if mid is the correct guess
            if m > 0 and m < (len(nums) - 1):
                if mid < nums[m - 1] and mid < nums[m + 1]:
                    return mid
            elif m < (len(nums) - 1):
                if mid > nums[m + 1]:
                    return nums[m + 1]
            elif m > 0:
                if mid < nums[m - 1]:
                    return mid

            # If mid isn't the correct guess, look on the correct half of the problem space
            if low <= mid and mid <= high:
                return low
            elif mid > high:
                l = m + 1
            else:
                r = m - 1
        
        return nums[l]