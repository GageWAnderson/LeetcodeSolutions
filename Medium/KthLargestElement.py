#If you could track the size of the heap, then you can easily use a fixed-size heap to track your search O(k) space, O(nlog(k)) time
class Solution:
    #Brute-force solution is to sort it and index O(nlogn)
    #Only need one pass through the array, so O(nk) worst-case time
    #Need to track the largest k elements seen so far,
    #Every new element I run into must be compared to the minimum of the list of largest elements
    #1. If the list of largest elements is shorter than k, add it in the appropriate place in that list
    #2. If that list is longer than k, compare x to the smallest element, if smaller don't add it
          #If larger, add it in the appropriate place in this list and kick out the smallest elements
        
    # At the end, return the kth element in the largest elements list
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargest = [] #index 0 is the maximum, end is the min in this list
        
        #.insert() inserts before the current element at that index
        def insertInOrder(intList, num):
            for i in range(len(intList)): #No -1 needed in this for expression
                if(num > intList[i]):
                    intList.insert(i,num)
                    return
            intList.append(num)
                
        for x in nums:
            insertInOrder(kLargest,x)
            if(len(kLargest) > k):
                kLargest.pop()
        
        return kLargest[k-1]

#Can upgrade from O(nk) to O(n) using the quick-select algorithm (related to quick-sort)
# O(nk) -> O(nlog(k)) -> O(n)

#O(nlog(k)) heap-based solution (last solution was really slow)
class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapSize = 0
        
        for x in nums:
            if(heapSize < k):
                heappush(heap,x)
                heapSize += 1
            else:
                top = heappop(heap)
                if(x > top):
                    heappush(heap,x)
                else:
                    heappush(heap,top)
            
        return heappop(heap)


#Best possible Solution uses quickSelect for an O(n) runtime with O(1) space
#Note: making the pivot random decreased runtime from ~3000ms to ~70ms !!!
class SolutionBest:
    import random
    #O(n) solution using the quickSelect algorithm
    #The current algo is destructive of the input
    #Should select a random pivot (this is best practice for partitioning)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 0,n-1
         
        while l <= r:
            pivotIndex = self.partition(nums,l,r)
            if(pivotIndex == n-k):
                return nums[pivotIndex]
            elif(pivotIndex > n-k): #answer is right of pivot Index
                r = pivotIndex - 1
            else: #answer is left of pivot index
                l = pivotIndex + 1
    
    def partition(self,List,l,r): #Quicksort partition function
        pivotIndex = random.randint(l,r)
        pivot = List[pivotIndex]
        self.swap(List,pivotIndex,r)
        i = l
        for j in range(l,r):
            if(List[j] < pivot):
                self.swap(List,i,j)
                i += 1
        self.swap(List,i,r) #Swap pivot to position i, found position for pivot
        return i #partition returns the position in the list for the pivot
    
    def swap(self,List,a,b):
        List[a],List[b] = List[b],List[a]
