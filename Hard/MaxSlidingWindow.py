#This fails on Leetcode because O(nk) isn't good enough for the time limit
#Note, even in sub-optimal runtime, I should still attempt the solution.
class SolutionBruteForce:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start,end = 0,k
        window = nums[start:end]
        n = len(nums)
        maxVals = [] #doing this in linear time may have to do with examining the return value
        #at each step
        
        while end <= n: #O(n)
            maxWindow = max(window) #O(k)
            maxVals.append(maxWindow)
            start += 1
            end += 1
            window = nums[start:end]
        
        return maxVals

#O(n) optimal solution for this problem uses a queue to keep track of the maximum
#In the sliding window






#Generic Sliding Window code:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() #mono (decreasing) queue 
        ans = []
        for i, x in enumerate(nums): 
            while queue and queue[-1][1] <= x: queue.pop() #only retaining larger than current value
            queue.append((i, x))
            if queue and queue[0][0] <= i-k: queue.popleft() #remove element outside of window 
            if i >= k-1: ans.append(queue[0][1])
        return ans 

#My rendition on the preceding block:

#Use the front of a deque to keep track of the maximum,
#This sliding window maximum is O(n) since each element is only examined at most twice
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if(k == 1): #Edge case
            return nums
        
        queue = deque()
        res = []
        
        for i,num in enumerate(nums):
            while queue and queue[-1][1] <= num: #keep elements on the left of the queue larger than x
                queue.pop() #Only retain elements larger than x
            queue.append((i,num))
            if queue and queue[0][0] <= i - k:
                queue.popleft() #Remove elements outside the window
            if i >= k - 1: #Only start appending the front of the queue at each iteration once first window traversed
                res.append(queue[0][1])
        return res