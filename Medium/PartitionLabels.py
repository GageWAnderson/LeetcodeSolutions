#Do parts have to be contiguous?
#As many parts as possible

#Use a counter on left,right sides to track which letters are present in a
#given section, create a new section once 2 sections become disjoint
from collections import Counter
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) == 1: return 1
        left = Counter()
        right = Counter(S) #O(N)
        res = []
        i,j = 0,0
        while j < len(S):
            right[S[j]] -= 1
            if right[S[j]] == 0:
                del right[S[j]]
            left[S[j]] += 1
            
            if left.keys().isdisjoint(right): #O(n)?
                res.append(j-i+1)
                left.clear() #New left side
                i = j+1
            j += 1
            
        return res

#Wiped the floor with this one!