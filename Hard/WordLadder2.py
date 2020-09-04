#Keep track of the path length so that when you find a path to the target,
#You only ever consider paths that are less than or equal to that target

#BFS, but with paths not words
#BFS gets the shortest paths in unweighted, undirected graphs
#Update the maximum path length whenever you find a solution
#At the end, trim all the solutions greater than the maximum path length
#No duplicates -> no self-loops

#This currently isn't backtracking properly -> easier to implement with recursive DFS
from collections import deque
class SolutionVerySlow: #O((big_constant)*ns)
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        maxLen = inf
        seen = set()
        res = []
        
        def getNbors(word):
            chars = "abcdefghijklmnopqrstuvwxyz"
            ans = []
            for i in range(len(word)):
                for c in chars:
                    newWord = (word[:i] + c + word[i+1:])
                    if newWord in wordSet and newWord not in seen:
                        ans.append(newWord)
            return ans
        
        #Now, do BFS to find the shortest paths, cap search at maxLen
        q = deque()
        q.append([beginWord])
        while q:
            currPath = q.popleft()
            seen.add(currPath[-1])
            if currPath[-1] == endWord:
                maxLen = min(maxLen,len(currPath))
                res.append(currPath)
                seen.remove(currPath[-1])
            elif len(currPath) >= maxLen:
                continue
            else:
                for nbor in getNbors(currPath[-1]):
                    newPath = currPath + [nbor]
                    q.append(newPath)
                    
        print(maxLen)
        return filter(lambda L:len(L) <= maxLen,res)#Function returns true to be kept in the result
    
    #To clear the relation between backtracking and DFS, we can say backtracking is a complete search technique and DFS is an ideal way to implement it.


    #BFS, but with paths not words
#BFS gets the shortest paths in unweighted, undirected graphs
#Update the maximum path length whenever you find a solution
#At the end, trim all the solutions greater than the maximum path length

#No duplicates -> no self-loops

#This currently isn't backtracking properly -> easier to implement with recursive DFS
from collections import deque, defaultdict
class SolutionSlow: #O((smaller_constant)*ns)
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        maxLen = inf
        seen = set()
        res = []
        
        adjList = defaultdict(list)
        for word in wordList: #O(ns)
            for i in range(len(word)):
                star = word[:i] + "*" + word[i+1:]
                adjList[star].append(word)

        def getNbors(word): #Constructing an adjacency list a priori removes a factor of 26 from the runtime
            ans = []
            for i in range(len(word)): #O(s), this mapping removes a const. factor of 26
                star = word[:i] + "*" + word[i+1:]
                for item in adjList[star]:
                    if item != word and item not in seen: #Don't forget to check seen
                        ans.append(item)
            return ans
        
        #Now, do BFS to find the shortest paths, cap search at maxLen
        q = deque()
        q.append([beginWord])
        while q:
            currPath = q.popleft()
            seen.add(currPath[-1])
            if currPath[-1] == endWord:
                maxLen = min(maxLen,len(currPath))
                res.append(currPath)
                seen.remove(currPath[-1])
            elif len(currPath) >= maxLen:
                continue
            else:
                for nbor in getNbors(currPath[-1]):
                    newPath = currPath + [nbor]
                    q.append(newPath)
        return filter(lambda L:len(L) <= maxLen,res)#Function returns true to be kept in the result
    
    #To clear the relation between backtracking and DFS, we can say backtracking is a complete search technique and DFS is an ideal way to implement it.