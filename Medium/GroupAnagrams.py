#You can make immutable sets as the keys for dictionaries using frozenset()
#That way, you can group anagrams using a dictionary in O(n) in one pass

#Very easy if you have an immutable multiset
#Can also do this with a default dictionary with the keys as counters of each char
from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()