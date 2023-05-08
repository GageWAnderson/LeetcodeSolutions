import heapq
from functools import cmp_to_key
class MedianFinder:

    def __init__(self):
        self.leftElementMaxHeap = []
        self.rightElementMinHeap = []
        self._keyFunc = cmp_to_key(self._compareNumsMaxHeap)

    def addNum(self, num: int) -> None:
        leftHeapSize, rightHeapSize = len(self.leftElementMaxHeap), len(self.rightElementMinHeap)
        median = self.findMedian()
        if median is None:
            heapq.heappush(self.rightElementMinHeap, num)
        elif num <= median: # Put num in the left max heap
            if leftHeapSize > rightHeapSize: # Re-balance the heaps if they are different sizes
                heapq.heappush(self.rightElementMinHeap, heapq.heappop(self.leftElementMaxHeap).obj)
            heapq.heappush(self.leftElementMaxHeap, self._keyFunc(num))
        else:
            if rightHeapSize > leftHeapSize: # Rebalance
                heapq.heappush(self.leftElementMaxHeap, self._keyFunc(heapq.heappop(self.rightElementMinHeap)))
            heapq.heappush(self.rightElementMinHeap, num)

        

    def findMedian(self) -> float:
        dataStreamLen = len(self.leftElementMaxHeap) + len(self.rightElementMinHeap)
        if dataStreamLen == 0:
            return None
        elif dataStreamLen % 2 == 0:
            left = self.leftElementMaxHeap[0].obj
            right = self.rightElementMinHeap[0]
            return (left + right) / 2
        else:
            if len(self.leftElementMaxHeap) > len(self.rightElementMinHeap):
                return self.leftElementMaxHeap[0].obj
            else:
                return self.rightElementMinHeap[0]
    
    def _compareNumsMaxHeap(self, n1, n2):
        if n1 < n2:
            return 1
        elif n1 == n2:
            return 0
        else:
            return -1


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()