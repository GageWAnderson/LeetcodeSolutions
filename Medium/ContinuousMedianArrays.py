#Uses 2 heaps to keep track of median continuously
import heapq
class Solution:
    def add_to_correct_heap(self,elem,lowers,uppers): #Also re-balances
        if lowers == [] and uppers == []:
            #Add first element to uppers
            heapq.heappush(uppers,elem)
        elif lowers == []:
            if elem < uppers[0]:
                heapq.heappush(lowers,elem)
            else:
                top = heapq.heappushpop(uppers,elem)
                heapq.heappush(lowers,top)
        elif uppers == []:
            if elem > lowers[0]:
                heapq.heappush(uppers,elem)
            else:
                top = heapq.heappushpop(lowers,elem)
                heapq.heappush(uppers,top)
        else:
            if elem > lowers[0]:
                heapq.heappush(uppers,elem)
            else:
                heapq.heappush(lowers,elem)
            #Rebalance sizes
            if len(lowers) > len(uppers) + 1:
                top = heapq.heappop(lowers)
                heapq.heappush(uppers,top)
            elif len(uppers) > len(lowers) + 1:
                top = heapq.heappop(uppers)
                heapq.heappush(lowers,top)

    def get_median(self,h1,h2):
        l1,l2 = len(h1),len(h2)
        if (l1+l2)%2 == 0:
            return (h1[0]+h2[0])/2 #Returns a float w/ avg. of 2 center elems
        else:
            if l1 > l2:
                return h1[0]
            else:
                return h2[0]

    def get_medians(self,A : List[int]) -> List[int]:
        lower_half = []
        upper_half = []
        medians = []
        for i in range(len(A)):
            curr = A[i]
            #This set of operations correctly shows code modularity
            #This is good code design, improves readability (Do more of this!)
            self.add_to_correct_heap(curr,lower_half,upper_half)
            medians.append(self.get_median(lower_half,upper_half))
            #Insert into lower half if curr < upper_half[0]
            #Insert into upper half if curr > lower_half[0]
            #In both cases, want to move the top of 1 heap to the other
        return medians
            

#Modularize FIRST during interviews, then implement stuff afterwards