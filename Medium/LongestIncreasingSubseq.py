#Either you take a given number or you don't
#O(2^n)
class SolutionSlow:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def helper(nums,maxSeen,pos):
            if pos == len(nums):
                return 0
            taken = 0
            if nums[pos] > maxSeen:
                taken = 1 + helper(nums,nums[pos],pos+1)
            notTaken = helper(nums,maxSeen,pos+1)
            return max(taken,notTaken)
        
        return helper(nums,-inf,0)

#Other than that, an O(N^2) solution is all I can come up with
#This is another problem that is recursive, with memoization downgrading complexity from (2^n) to (n^2)

#Every time you run into a new number, you can either take it or not take it
class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
            if not nums:
                return 0
            dp = [1]*len(nums)
            dp[-1] = 1
            for i in reversed(range(len(nums))):
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)

#Optimal solution uses Binary Search to get O(nlogn) -> This is a tough solution 
#Cannot be expected in an interview

#Now for my DP solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        dp = [1 for x in range(len(nums))]
        
        for j in range(1,len(nums)):
            maxBeforeJ = 0
            for i in range(j):
                if nums[j] > nums[i]:
                    maxBeforeJ = max(maxBeforeJ,dp[i])
            dp[j] = maxBeforeJ + 1
        return max(dp)