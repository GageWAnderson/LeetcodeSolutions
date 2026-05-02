class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # NOTE: A left-rotated array is 2 sorted arrays concatenated
        # The first sortest array is strictly greater than the second
        # NOTE: That in the trivial case where the array isn't rotated this returns to regular binary search
        left, right = 0, len(nums) - 1

        # NOTE: Binary search turns into an infinite loop easily if you do `left <= right` instead of left < right

        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                # Left side is sorted
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right side is sorted
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums[left] == target else -1
