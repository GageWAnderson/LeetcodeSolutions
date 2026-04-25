class SolutionSorting:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for interval in intervals:
            points.append((interval[0], 1)) # Start Point
            points.append((interval[1], 0)) # End Point
        points.sort()
        print(points)

        # O(nlogn) time, O(n) space to sort and combine start, endpoints
        currNumRooms = 0
        maxNumRooms = 0
        for point in points:
            if point[1] == 1: # Start Point
                currNumRooms += 1
            else: # End point
                maxNumRooms = max(maxNumRooms, currNumRooms)
                currNumRooms -= 1
        
        return maxNumRooms

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        endpoint_heap = []
        max_num_rooms = 0
        
        intervals.sort() # O(nlog(n)) time, O(n) space

        for interval in intervals: # O(nlogn) time, O(n) space
            while endpoint_heap and endpoint_heap[0] <= interval[0]:
                heapq.heappop(endpoint_heap)
            heapq.heappush(endpoint_heap, interval[1])
            max_num_rooms = max(max_num_rooms, len(endpoint_heap))
        
        return max_num_rooms