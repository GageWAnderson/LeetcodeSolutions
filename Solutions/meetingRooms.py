class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i,interval in enumerate(intervals):
            if i > 0 and intervals[i - 1][1] > interval[0]:
                return False
        
        return True