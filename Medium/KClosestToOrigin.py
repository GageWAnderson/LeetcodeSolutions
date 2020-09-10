from functools import cmp_to_key
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def compare(x : List[int], y : List[int]):
            distX = x[0]**2 + x[1]**2
            distY = y[0]**2 + y[1]**2
            if distX < distY:
                return -1
            elif distX > distY:
                return 1
            else:
                return 0
        
        points.sort(key = cmp_to_key(compare))
        return points[:K]
        
#This is a repeated quick-select problem
import heapq
class Point:
    def __init__(self,pair):
        self.x = pair[0]
        self.y = pair[1]
        self.dist = self.x**2 + self.y**2
    
    def __lt__(self,other):
        return self.dist < other.dist
    
    def toList(self):
        return [self.x,self.y]
    
class SolutionHeap:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        minHeap = []
        def dist(p):
            return p[0]**2 + p[1]**2
        
        for point in points:
            heapq.heappush(minHeap,Point(point))
        
        res = []
        i = 0
        while minHeap and i < K:
            res.append(heapq.heappop(minHeap).toList())
            i += 1
        return res