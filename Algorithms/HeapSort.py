import heapq
class HeapSort:
    '''
    Loops through list and enters all elements into a min-heap, extracts elements
    into a newly ordered list.
    Time: O(nlogn)
    Space: O(n) (heap requires this much space)
    '''
    def __init__(self):
        self.id = 0
    
    def heapSort(self, L):
        heapq.heapify(L)
        return heapq.nsmallest(len(L), L) #O(nlogn) + O(n), min heap
    
if (__name__ == "__main__"):
    hs = HeapSort()
    hardCode1 = [4,3,2,5,6,7,12,7,77,7,65,4,5,6,]
    print(hs.heapSort(hardCode1))