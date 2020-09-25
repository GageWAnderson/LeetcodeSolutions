#I had no idea about the topological sort algorithm, that's why I was so lost on this
#problem, now that I know the top_sort algo the solution is more clear
from collections import defaultdict
class Solution:
    def makeLetterGraph(self,words):
        graph = {c : [] for word in words for c in word}
        for word_one, word_two in zip(words,words[1:]):
            for c,d in zip(word_one,word_two):
                if c != d:
                    graph[c].append(d)
                    break
            else: #Make sure the second word isn't a prefix of the first
                if len(word_two) < len(word_one):
                    return None
        return graph
                
    def alienOrder(self, words: List[str]) -> str:
        graph = self.makeLetterGraph(words)
        #print(graph)
        if not graph: return "" #No prefixes allowed after a given word
        if self.detectCycleDirected(graph): return ""
        
        seen = {l : False for l in graph}
        stack = []
        
        def topologicalSort(v,s):
            seen[v] = True
            for l in graph[v]:
                if seen[l] == False:
                    topologicalSort(l,s)
            s.append(v)
        
        for l in graph:
            if seen[l] == False:
                #print(f"stack = {stack}")
                topologicalSort(l,stack)
                
        res = reversed(stack)
        return "".join(res)
    
    #Returns true if any back-edges are detected in the graph
    def detectCycleDirected(self,graph):
        visited = {l : False for l in graph}
        rec_stack = {l : False for l in graph}
        
        def dfs(node):
            visited[node] = True
            rec_stack[node] = True
            for nbor in graph[node]:
                if rec_stack[nbor] and visited[nbor]:
                    return True
                elif visited[nbor]:
                    continue
                else:
                    if dfs(nbor):
                        return True
            rec_stack[node] = False
            return False
        
        return dfs(list(graph.keys())[0])
        
#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.