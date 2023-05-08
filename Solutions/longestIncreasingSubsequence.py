"""
Bottom-up solution doesn't always have to be backwards.
Can be forwards as well (easier, simpler code that way).
Made the mistake of going backwards when I didn't need to.
"""
class SolutionBottomUpDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

"""
Almost had this one, didn't take max(dp) at the end 
"""
class SolutionBottomUpDPBackwards:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)

"""
Optimal Solutions use Binary Search (very clever).
Interviewers won't expect you to get stuff like this on the first try,
  would need a hint if you haven't seen before.
"""
class SolutionOptimal: # O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)