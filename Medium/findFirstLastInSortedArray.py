#It is more clean to do 2 regular, modified binary searches for the first and last occurance of target,
#Rather than finding any target and expanding from there (hard and confusing)

#You can also make this code more modular for readability
def findFirst(nums,target):
    lower,upper = 0,len(nums)-1 #Just start upper as the last index
    while lower+1 < upper:
        mdpt = lower + (upper - lower)//2
        if nums[mdpt] < target: lower = mdpt
        else: upper = mdpt
    if nums[lower] == target: return lower
    else: return -1

def findLast(nums,target):
    lower,upper = 0,len(nums)
    while lower+1 < upper:
        mdpt = lower + (upper - lower)//2
        if nums[mdpt] <= target: lower = mdpt #equals sign causes lower bound to move up through the run of numbers
        else: upper = mdpt
    if nums[lower] == target: return lower
    else: return -1 #Remember to write the final return statement when you're doing this on paper!!!

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums) == 0): return [-1,-1] #Clean up the input
        lower = findFirst(nums,target)
        
        #Optimization: if findFirst returns -1, don't run findLast
        if lower == -1: return [-1,-1]
        else:
            upper = findLast(nums,target)
            return [lower,upper]