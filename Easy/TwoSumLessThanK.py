#There is a solution in O(m + n) called counting sorts where Two pointers
#Enumerate all the pairs in the limited range of points (LOTS OF SPACE)
#All the best solutions are O(nlogn), particularly binary search

#The best solution for this is the 2-Sum two pointers style (Only works on sorted lists)
class Solution: #O(nlogn) solution because of the heap
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if len(A) <= 1: return -1
        A.sort() #O(nlogn)
        curr_sum = -1
        
        p1,p2 = 0,len(A)-1
        
        while p1<p2:
            if A[p1]+A[p2] < K:
                curr_sum = max(curr_sum,A[p1]+A[p2])
                
            if A[p1]+A[p2] < K:
                p1 += 1
            elif A[p1]+A[p2] >= K:
                p2 -= 1
        
        return curr_sum