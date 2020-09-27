#This is the merge intervals problem
#Note that the input is unsorted, O(nlogn) minimum ?

#I was right to suggest O(nlogn) for an upper bound
#However, I tried to over-simplify this (should have considered start,end times seperately)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        if len(intervals) == 1: return 1
        n = len(intervals)
        res = 0
        
        starts = sorted(i[0] for i in intervals) #O(nlogn)
        ends = sorted(i[1] for i in intervals) #O(nlogn)
        
        start_p, end_p = 0,0
        
        while start_p < n:
            if starts[start_p] >= ends[end_p]:
                res -= 1
                end_p += 1
            
            res += 1
            start_p += 1
                
        return res