class Solution:
    """
    Overcomplicated my first solution using a heap. Can get away with a greedy
    solution if I properly 
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end # No overlap, continue
            else:
                res += 1
                # GREEDY: Take off the larger of the 2 intervals by endpoint
                prevEnd = min(end, prevEnd)
        
        return res