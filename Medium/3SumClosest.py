class Solution:
    #O(n^3) solution, need to look at all combonations
    #Doesn't work for negative targets, need to compare with abs vals
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")
        res = float("inf")
        
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i+1,len(nums)):
                num2 = nums[j]
                
                #Now do 2-sum
                for k in range(j+1,len(nums)):
                    curr_sum = num1 + num2 + nums[k]
                    diff = abs(target - curr_sum)
                    if diff < closest:
                        res = curr_sum
                        closest = diff
                    if curr_sum == target:
                        return curr_sum
                    
        return res

class SolutionBest:
    # Use two-pointers method with sorting, can get O(n^2) time complexity
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')  # Initialize difference to infinity
        nums.sort()  # Sort the array to enable two-pointer approach
        
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1  # Initialize two pointers
            
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]  # Calculate current sum
                
                # Update diff if current sum is closer to target
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                
                # Move pointers based on sum comparison with target
                if sum < target:
                    lo += 1  # Increase sum by moving left pointer right
                else:
                    hi -= 1  # Decrease sum by moving right pointer left
            
            # If exact match found, no need to continue
            if diff == 0:
                break
        
        return target - diff  # Return the closest sum

