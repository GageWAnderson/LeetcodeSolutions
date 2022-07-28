from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqMapS = defaultdict(int)
        freqMapT = defaultdict(int)
        for char in s:
            freqMapS[char] += 1
        for char in t:
            freqMapT[char] += 1
        
        for char in s:
            if freqMapS[char] != freqMapT[char]:
                return False
        return True