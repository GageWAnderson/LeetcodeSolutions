#Brute force is to look at every single element and examine how many elements on either side
#Of it are contiguous with that element and are greater than or equal to that element
#The max for that index is the size of that window multiplied by heights[index]
#This is O(n^2)
class SolutionBad:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxVal = 0
        for i in range(len(heights)):
            n = heights[i]
            print(f"n = {n}")
            start = end = i
            while(start-1 >= 0 and heights[start-1] >= n):
                start -= 1
            while(end+1 < len(heights) and heights[end+1] >= n):
                end += 1
            
            if(n*(end-start+1) > maxVal):
                print(start)
                print(end)
                maxVal = n*(end-start+1)
        
        return maxVal
        
#Monotonous stack solution (copied good solution)
class SolutionBest:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Calculate the rectanglar area which determined by the popped bar: 
		width =  [stack top after popping] + 1 to cur - 1
		height = popped bar
        """
        rst = 0
        increaseStack = []
        heights.append(0) # help to pop out the final increasing bars
        for i, h in enumerate(heights):
            while increaseStack and h <= heights[increaseStack[-1]]:
                heightBarPos = increaseStack.pop()
                start = increaseStack[-1] + 1 if increaseStack else 0
                end = i - 1
                width = end - start + 1
                rst = max(rst, width * heights[heightBarPos])
            increaseStack.append(i)
        return rst     


#The best solution for this problem uses 2 stacks
#Stacks are used since positions are examined FIFO order
#The rectangles are started at a given position and ended when you reach
#A bar of lower height than where you started 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        posStack = []
        heights.append(0)
        for i,h in enumerate(heights):
            while posStack and heights[posStack[-1]] > h:
                currHeightPos = posStack.pop()
                start = posStack[-1] + 1 if posStack else 0
                end = i - 1
                width = end - start + 1
                res = max(res, width*heights[currHeightPos])
            posStack.append(i)
        return res