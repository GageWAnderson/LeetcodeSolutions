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