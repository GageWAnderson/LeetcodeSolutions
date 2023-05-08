"""
There is also a Union Find Solution, but that one isn't optimal.
Can reduce the memory complexity to O(1) extra space by looking
at the endpoint at the end of res and comparing it to the start.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        
        startPoints, endPoints = [], []
        for interval in intervals:
            startPoints.append(interval[0])
            endPoints.append(interval[1]) # O(n)
        startPoints.sort()
        endPoints.sort() # O(nlogn)

        res = []
        currInterval = []
        numOverlappingIntervalsInCurr = 0
        s,e = 0,0

        while s < n or e < n:
            if s < n and startPoints[s] <= endPoints[e]: # Consider a start point
                if not currInterval:
                    currInterval.append(startPoints[s])
                numOverlappingIntervalsInCurr += 1
                s += 1
            else: # Consider an end point
                numOverlappingIntervalsInCurr -= 1
                if numOverlappingIntervalsInCurr == 0:
                    # Reset the current interval and append it to res
                    currInterval.append(endPoints[e])
                    res.append(currInterval)
                    currInterval = []
                e += 1
        
        return res

class SolutionOptimal: # O(nlogn) time, O(n) space, O(1) extra space
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key = lambda i : i[0])
        res = []
        res.append(intervals[0])
        for start,end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res