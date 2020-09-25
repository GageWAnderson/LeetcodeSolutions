class SolutionTwoPointers:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            return s if nums[0] >= s else 0
        
        i,j = 0,0
        min_dist = float("inf")
        curr_sum = nums[0]
        while i < n and j < n:
            if j-i == 0 and curr_sum >= s:
                return 1
            elif curr_sum >= s:
                min_dist = min(min_dist,j-i+1)
                curr_sum -= nums[i]
                i += 1
            elif curr_sum < s:
                j += 1
                if j < n:
                    curr_sum += nums[j] 
                
        return min_dist if min_dist < float("inf") else 0