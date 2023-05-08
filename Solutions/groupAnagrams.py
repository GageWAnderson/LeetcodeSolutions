from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        def constructFreqFrozenSet(counter):
            res = set()
            for c in counter:
                res.add(c + str(counter[c]))
            return frozenset(res)

        for word in strs:
            freqCounter = Counter(word)
            freqKey = constructFreqFrozenSet(freqCounter)
            anagramDict[freqKey].append(word)
        
        res = []
        for freqCounter in anagramDict:
            res.append(anagramDict[freqCounter])
        return res

from collections import defaultdict,Counter
class SolutionClean:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()