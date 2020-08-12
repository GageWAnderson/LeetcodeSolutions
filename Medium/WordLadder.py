#This problem can be viewed as a graph, with the neibhors of a vertex being words with only
#1 letter different from given word
#Then all you have to do is get the length of the shortest path using BFS

#BFS is used here because the graph is unweighted


class Node:
    def __init__(self,val=None,level=None):
        self.val = val
        self.level = level
    
    def __repr__(self):
        return f"val = {self.val}, level = {self.level}"

#This solution O((E+V)ns), which is very slow...
#Could make an explicit graph... O(n^2) and uses lots of space
#Definitely can improve oneAway by using a Trie...
class SolutionSlow:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        visited = set()
        queue.append(Node(beginWord,1))
        while queue: #BFS is O(E + V)
            vertex = queue.popleft()
            level = vertex.level
            if(vertex.val == endWord):
                return level
            
            if vertex.val not in visited: #O(1)
                visited.add(vertex.val)
                nbors = self.getNbors(vertex,wordList) # O(ns), this is slowing me down
                
                for nbor in nbors:
                    queue.append(nbor)
        return 0
    
    def getNbors(self,vertex,wordList):
        res = []
        for word in wordList:
            if self.oneAway(vertex.val,word): #O(s), where s is the len of short string
                res.append(Node(word,vertex.level+1))
        return res
    
    #Maybe can use a Trie to get oneAway to O(log(s)) instead of O(s)
    def oneAway(self,w1,w2):
        if len(w1) != len(w2): return False
        diffCount = 0
        for i,letter in enumerate(w1):
            if(w2[i] != letter):
                diffCount += 1
            if(diffCount > 1):
                return False
        return True

#Speed this up by turning word-list into a set for constant time lookups

#This problem can be viewed as a graph, with the neibhors of a vertex being words with only
#1 letter different from given word
#Then all you have to do is get the length of the shortest path using BFS
        
class SolutionBetter: #O((E+V)*26*s)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList) #O(n)
        queue = deque()
        visited = set()
        queue.append(Node(beginWord,1))
        while queue: #BFS is O(E + V)
            vertex = queue.popleft()
            level = vertex.level
            if(vertex.val == endWord):
                return level
            
            if vertex.val not in visited: #O(1)
                visited.add(vertex.val)
                nbors = self.getNbors(vertex,wordSet) # O(26s)
                
                for nbor in nbors:
                    queue.append(nbor)
        return 0
    
    def getNbors(self,vertex,wordSet): #O(26*s) due to constant-time lookup
        res = []
        for i in range(len(vertex.val)): #O(s)
            for c in "abcdefghijklmnopqrstuvwxyz": #O(26)
                newWord = vertex.val[:i] + c + vertex.val[i+1:]
                if newWord in wordSet: #O(1)
                    res.append(Node(newWord,vertex.level+1))
        return res