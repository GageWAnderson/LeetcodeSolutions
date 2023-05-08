"""
Keys to this problem:
1. Recognize the sliding window (maximize x over an array)
2. Try all 3 methods of sliding window
  a. Two pointers start at 0
  b. Two pointers go out from middle
  c. Two pointers go in from outside
3. Find the greedy choice you can make at each step to move one of the pointers.

The point of these problems is to move the pointers in such a way to look at the
solution space of order O(n) first to avoid having to examine all n^2 solutions.
  - We can figure out that prioritizing 1. distance apart (outside-in) and 
    2. height will have us look at all the best solutions in our first pass

Overall, you can guess that there will be a two-pointers optimization from the 
metagame of them asking a question like this. Your job is to figure out what
type of sliding window to use and what the trick is to move the pointers at each step.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r = 0, len(height) - 1
        maxWater = 0

        while l < r:
            currWater = (r - l)*min(height[l], height[r])
            maxWater = max(maxWater, currWater)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater