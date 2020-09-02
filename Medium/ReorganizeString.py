#Put all the letters in a multiset, then empty the multiset into a new max-heap
#Build up the string by alternating the maximum 2 elements in the heap

#Criterion for returning "" -> if one member of the set takes up more than half the space
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        if n <= 1: return S
        max_count = (n//2) if n%2==0 else (n//2+1)
        counter = Counter(S)
        most_common = counter.most_common()
        most_common = [(-most_common[i][1],most_common[i][0]) for i in range(len(most_common))]
        heapq.heapify(most_common) #heapify returns None
        
        if -most_common[0][0] > max_count: return ""
        sb = []
        while most_common:
            if len(most_common) == 1:
                top = heapq.heappop(most_common)
                sb.append(top[1])
            else:
                top = heapq.heappop(most_common)
                second = heapq.heappop(most_common)
                sb.append(top[1])
                sb.append(second[1])
                
                new_top = (top[0]+1,top[1])
                new_second = (second[0]+1,second[1])
                if new_top[0] != 0:
                    heapq.heappush(most_common,new_top)
                if new_second[0] != 0:
                    heapq.heappush(most_common,new_second)
        
        return "".join(sb)