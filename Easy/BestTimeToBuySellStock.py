#Brute force is O(n^2) where you look at all the intervals
#Heap approach to keep track of the maximum and minimum elements available at every point would work O(nlogn)

class SolutionOverthinking: #O(nlogn)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        #Push (index,price) tuples onto the heaps and record pointers to them
        #For constant-time removal from heaps
        minHeap = [] #Present and past prices
        maxHeap = [] #Future Prices
        maxHeapEntries = dict()
        
        for i,price in enumerate(prices):
            thisPrice = [-price,i] #Negative since this is a max heap
            maxHeapEntries[i] = thisPrice
            heapq.heappush(maxHeap,thisPrice)
        
        maxDiff = 0 #Defaut is zero since you don't have to sell the stock
        for j,price in enumerate(prices):
            if j == len(prices)-1: break
            print(f"j = {j}")
            #Delete the current element from the max heap and place it in the min heap
            maxHeapEntries[j][1] = -inf
            heapq.heappush(minHeap,[price,j])
            
            #Now compare the 2 elements and update maxDiff
            #print(f"minHeap = {minHeap}")
            #print(f"maxHeap = {maxHeap}")
            currMin = self.getTop(minHeap)[0]
            currMax = -self.getTop(maxHeap)[0] #Remember these elements were entered as negative
            #print(f"currMax = {currMax}, currMin = {currMin}")
            newDiff = currMax - currMin
            if newDiff > maxDiff:
                maxDiff = newDiff
        
        return maxDiff
    
    def getTop(self,heap):
        while heap:
            top = heapq.heappop(heap)
            if top[1] != -inf:
                heapq.heappush(heap,top) #Forgot to add back to the heap
                return top
            
        raise Exception("Heap is empty")
        
#Lesson: inserting lists into heapq heaps determines the value of each list by sequentialy
#Comparing the elements so all the elements must be integers

class SolutionOnePass: