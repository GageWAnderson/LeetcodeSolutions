from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m,n = len(s),len(t)

        # Multiset/Bag/Counter of letters in t
        tFreqMap = defaultdict(int)
        for c in t:
            tFreqMap[c] += 1
        
        def f1SubsetOfF2(f1, f2): # O(52) comparison time in this case
            for item in f1:
                if f1[item] > f2[item]:
                    return False
            return True

        lettersInWindow = defaultdict(int)
        l,r = 0,0
        minSubstringLen = float('inf')
        minSubstringPointers = None
        while r < m:
            if r < m:
                lettersInWindow[s[r]] += 1

            while f1SubsetOfF2(tFreqMap,lettersInWindow):
                if (r - l + 1) < minSubstringLen:
                    minSubstringPointers = (l, r)
                    minSubstringLen = r - l + 1
                lettersInWindow[s[l]] -= 1
                l += 1
            
            r += 1
        
        return s[minSubstringPointers[0]:minSubstringPointers[1] + 1] if minSubstringPointers else ""