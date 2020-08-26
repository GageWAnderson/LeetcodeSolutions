class SolutionSlidingWindow: #O(n), O(1) space optimal solution
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        p1,p2 = 0, len(height) - 1
        maxA = 0
        
        while p1 < p2: #This is a common sliding window pattern
            bucket = min(height[p2],height[p1])*(p2-p1)
            maxA = max(maxA,bucket)
            if height[p1] < height[p2]: #Move the one with the lower height, less maxima calculations
                p1 += 1
            else:
                p2 -= 1
            #print(f"big = {bucketBig}, left = {bucketLeft}, right = {bucketRight}")
        
        return maxA