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

#Month later, crush this in less than an hour on my first try!
#Remembered that you need to use a stack, annoying to deal with edge-cases
class Solution:
    def trap(self, height: List[int]) -> int:
        decStack = []
        res = 0
        
        for i,num in enumerate(height):
            if not decStack or num < decStack[-1][0]:
                decStack.append((num,i))
            else:
                while decStack and decStack[-1][0] <= num:
                    h1,i1 = decStack.pop()
                    if decStack:
                        h0,i0 = decStack[-1]
                        height = min(h0,num)-h1
                        width = i - i0 - 1
                        res += height*width
                decStack.append((num,i))
                
        return res