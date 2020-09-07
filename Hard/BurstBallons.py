#The top-down DP solution makes the most sense to me
#This problem uses the divide/conquer technique to split up the left/right sides
#memoize the answer from div/conquer
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = dict() #(left,right) -> sum
        nums = [1] + nums + [1] #Gets rid of edge-cases
        
        def helper(left,right):
            if left + 1 == right:
                return 0
            elif (left,right) in dp:
                return dp[(left,right)]
            else:
                maxVal = -inf
                for i in range(left+1,right):
                    thisScore = nums[left]*nums[i]*nums[right] + helper(i,right) + helper(left,i)
                    maxVal = max(maxVal,thisScore)
                dp[(left,right)] = maxVal
                return maxVal
        
        return helper(0,len(nums)-1)

#DP + divide/conquer solution