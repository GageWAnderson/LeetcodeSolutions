from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFreqMap = defaultdict(int)
        tFreqMap = defaultdict(int)
        for i in range(len(s)):
            sFreqMap[s[i]] += 1
            tFreqMap[t[i]] += 1
        
        for letter in sFreqMap:
            if tFreqMap[letter] != sFreqMap[letter]:
                return False
        return True