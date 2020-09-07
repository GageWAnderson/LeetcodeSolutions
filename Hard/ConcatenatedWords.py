#Very similar to word break, need to do DFS on each word (word.startswith(entry))
#Append string to res when you get to the base case
class SolutionSlowDFS:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words) <= 1: return []
        
        res = []
        resSet = set() #No duplicates
        
        def dfs(currWord,startIndex):
            if startIndex == len(currWord):
                resSet.add(currWord)
            else:
                for word in words: 
                    if word != "" and word != currWord and currWord[startIndex:].startswith(word):
                        dfs(currWord,startIndex+len(word))
                        
        for word in words:
            if word != "": #Need to check for the empty string
                dfs(word,0)
        return list(resSet)

#Almost got this first try, just needed to control for duplicates/empty string
#There is also a solution using a Trie I didn't think of