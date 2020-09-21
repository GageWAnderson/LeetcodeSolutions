#Got this question, but with numbers in a Code Screen
#This is a graph search problem
#Just make an explicit graph and traverse it depth-first

#Wasn't handling duplicates properly...
#Need to use a bitmap to account for duplicate airports under a single start
from collections import defaultdict
import copy
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        graph = defaultdict(list)
        curr = []
        self.output = None #Use self. to make class globals
        #Need to track edges visited, not nodes visited
        self.visited = defaultdict(list)
        
        #Remember to sort the adj. list alphabetically
        def makeGraph(): #Adj. list format
            for tick in tickets:
                graph[tick[0]].append(tick[1])
                self.visited[tick[0]].append(0) #Initialize visited (works with duplicates)
            #Sort each list to ensure lexical order
            for key in graph:
                graph[key].sort()
        
        def dfs(start,depth):
            if depth == n+1:
                curr.append(start)
                self.output = copy.deepcopy(curr)
                return True
            else:
                curr.append(start)
                for i,nbor in enumerate(graph[start]):
                    if self.visited[start][i] == 0:
                        self.visited[start][i] = 1
                        if dfs(nbor,depth+1):
                            return True #Exit early (greedy)
                        self.visited[start][i] = 0
                curr.pop()
                return False
                
        makeGraph()
        dfs("JFK",1)
        return self.output