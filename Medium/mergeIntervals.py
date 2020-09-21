class Solution: #O(nlog(n)), this problem can also be solved via a graph connected components strategy
    def canMerge(self,curr,next):
        return curr[1] >= next[0]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0]) #O(nlog(n)) THIS LINE SAVED ME
        res = []
        curr = 0
        next = 0
        end = len(intervals)
        while curr < end:
            merged = False
            merge = intervals[curr] #Dealing with vectors! not curr[1], intervals[curr][1]
            #Also, remember that tuples are immutable!!!
            next = curr + 1
            while next < end and self.canMerge(merge,intervals[next]): #need short-circuit evaluation here...
                merged = True
                merge[1] = max(intervals[next][1],intervals[curr][1]) #Need to account for intervals contained within                                                                              #the current interval
                next += 1
            
            if merged: res.append(merge)
            else: res.append(intervals[curr])
            curr = next
        return res

class SolutionBest:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            elif merged[-1][1] >= interval[0]:
                merged[-1][1] = max(interval[1],merged[-1][1])
            else:
                merged.append(interval)
        return merged