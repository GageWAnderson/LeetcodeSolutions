#Keep track of the path length so that when you find a path to the target,
#You only ever consider paths that are less than or equal to that target
class Node:
    def __init__(self,val="",level=0):
        self.val = val
        self.level = level
    
    def __repr__(self):
        return f"val = {self.val}, level = {self.level}"

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        queue = deque()
        queue.append([Node(beginWord,1)])
        wordSet = set(wordList) #O(n)
        seen = set()
        res = []
        maxLevel = inf
        
        while queue: #O(E + V)
            currPath = queue.popleft()
            currNode = currPath[-1]

            if currNode.val == endWord:
                res.append(currPath)
                maxLevel = currNode.level
                continue
            
            if currNode.level < maxLevel and currNode not in seen:
                seen.add(currNode.val)
                
                nbors = self.getNbors(currNode,wordSet,seen) #O(26s)
                for nbor in nbors:
                    newPath = currPath + [nbor]
                    queue.append(newPath)
        return self.getShortestPaths(self.getPaths(res))
    
    def getShortestPaths(self,pathList):
        minLen = inf
        res = []
        for path in pathList:
            if len(path) < minLen:
                minLen = len(path)
        for path in pathList:
            if len(path) == minLen:
                res.append(path)
        return res
    
    def getPaths(self,pathList):
        ans = []
        def getPath(L):
            res = []
            for node in L:
                res.append(node.val)
            return res
        
        for path in pathList:
            ans.append(getPath(path))
        return ans
    
    def getNbors(self,vertex,wordSet,seen): #O(26*s)
        res = []
        for i in range(len(vertex.val)): #O(s)
            for c in "abcdefghijklmnopqrstuvwxyz": #O(26)
                newWord = vertex.val[:i] + c + vertex.val[i+1:]
                if newWord not in seen and newWord in wordSet: #O(1)
                    res.append(Node(newWord,vertex.level+1))
        return res