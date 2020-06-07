#NOTE: Stacks can be efficiently implemented with lists using .append() and .pop(), however
#queues need the efficient deque function to get fast speed for removing from beginning (.popleft()) and end (.pop())
#https://www.geeksforgeeks.org/stack-and-queues-in-python/
from collections import deque
class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        volume,i = 0,0
        
        while i<len(heights):
            #top = stack[-1] #Need to check if empty first!
            while(len(stack) > 0 and heights[i] > heights[stack[-1]]):
                top = stack.pop()
                if(len(stack) == 0): 
                    break
                newTop = stack[-1] #I wish there was a builtin to get the last element in a list
                #There is! stack[-1]
                distance = i - newTop -1
                depth = min(heights[i],heights[newTop]) - heights[top]
                volume += distance * depth
            
            stack.append(i)
            i += 1
        
        return volume