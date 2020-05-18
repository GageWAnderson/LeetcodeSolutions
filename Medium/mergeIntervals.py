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

class SolutionElegant: #Same type of solution, just more succinct
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged