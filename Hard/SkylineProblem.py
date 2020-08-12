#Input list is already sorted in ascending order of left x positions
#Output must be in ascending order of x position

#This is a hard and confusing problem, do the brute force first
#Brute force looks at every x coordinate from 0 to maximum x coordinate
#And determines the max at that coordinate by looking at all the buildings
#Whenever the max is different from that at the previous x coordinate, update keyPoints
    #The skyline level is the maximum height of all the buildings at that x coordinate
    #So whenever the maximum height changes, we have a new key point

#Intuited that a heap would be a good data structure
#Also that looping through buildings instead of x-coordinates would be necessary. 
#NOTE: Just push negative numbers onto python heaps in order to make it a max-heap
#GOAL: Do this problem in O(nlog(n))

#Tree-map data structure supports remove in log(n) time, max-heap does not
#Tree-map keeps track of both max/min as well as order of insertion with log(n)
  #Insertion/removal times (I have run into this requirement multiple times)
#Every time you encounter the start of a new building, push its height into a max heap
#If the maximum changes, we have found a key point, so add it to the result

#When you encounter the end of a building, you need to remove that building from the heap

#The challenge is to properly list the start and end points of all the buildings
#So that their maxima are examined in the correct order by the heap

#Visually, I know the optimal solution O(nlogn)
#So loop through all the buildings and make a decision about whether or not to include a key point for each building
class buildingPoint:
    def __init__(self,x,h,isStart):
        self.x = x
        self.h = h
        self.isStart = isStart


    def __lt__(self,other): #This logic controls for edge-cases
        if not other:
            return True
        if self.x != other.x:
            return self.x < other.x
        else:
            if self.isStart and other.isStart:
                return self.h > other.h
            elif not self.isStart and not other.isStart:
                return self.h < other.h
            else:
                return self.isStart
    
    def __repr__(self):
        return f"x = {self.x}, h = {self.h}, isStart = {self.isStart}"
    
class Solution:
    import heapq
        
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0: return []
        maxHeights = [] #Holds all the building heights at a given point
        keyPoints = []
        buildingPoints = self.getBuildingPoints(buildings)
        for bp in buildingPoints: #building points must be properly sorted
            prevMax = heapq.nlargest(1,maxHeights)[0] if maxHeights else 0
            if bp.isStart:
                heapq.heappush(maxHeights,bp.h)
                newMax = heapq.nlargest(1,maxHeights)[0] if maxHeights else 0 #nlargest(n,heap) returns a list
                if newMax != prevMax: #If the maximum height changes, add the key point
                    keyPoints.append([bp.x,newMax])
            else:
                maxHeights.remove(bp.h) #Remove the start and end points for that building
                newMax = heapq.nlargest(1,maxHeights)[0] if maxHeights else 0
                if newMax != prevMax:
                    keyPoints.append([bp.x,newMax])
        return keyPoints
    
    def getBuildingPoints(self,buildings):
        res = []
        for l,r,h in buildings:
            res.append(buildingPoint(l,h,True))  #Start point
            res.append(buildingPoint(r,h,False)) #End point
        res.sort() #Returns None, void method
        return res #O(nlogn), __lt__ controls order of points