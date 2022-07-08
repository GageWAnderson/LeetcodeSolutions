from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDictLength = len(wordsDict)
        self.wordIndicies = defaultdict(list)
        for i in range(len(wordsDict)):
            self.wordIndicies[wordsDict[i]].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        minDistance = self.wordsDictLength + 1 # Greatest possible distance + 1
        word1Indicies, word2Indicies = self.wordIndicies[word1], self.wordIndicies[word2]
        
        i,j = 0,0
        while i < len(word1Indicies) and j < len(word2Indicies):
            dist = abs(word2Indicies[j] - word1Indicies[i])
            minDistance = min(dist, minDistance)
            if word1Indicies[i] < word2Indicies[j]:
                i += 1
            else:
                j += 1
        return minDistance

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)