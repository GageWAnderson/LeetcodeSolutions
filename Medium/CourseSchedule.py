#prerequisites is an adjacency list explicit graph
#This is a graph traversal problem, need to be able to reach all the nodes to return true
#The graph is directed due to prerequisites
#You start at course #0?
#Cycles are death! Any cycles in this graph mean you can't finish
  #Use DFS to detect cycles

#Q: are the prereqs sorted (proper adj list format?)
#Got the concept entirely right, but I had no Idea how to do a graph-cycle-detection algorithm
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []: return True
        nodes = range(numCourses)
        visited = set()
        recStack = set()
        
        for node in nodes:
            if node not in visited:
                if self.isCyclic(node,visited,recStack,prerequisites):
                    return False
        return True
    
    def isCyclic(self,node,visited,recStack,graph):
        #Mark node as visited and add to the recStack
        visited.add(node)
        recStack.add(node)
        
        #Recur for all nbors, if any nbors are visited and in recStack, graph is cyclic
        for nbor in self.getNbors(node,graph):
            if nbor not in visited:
                if self.isCyclic(nbor,visited,recStack,graph):
                    return True
            elif nbor in recStack:
                return True
        
        recStack.remove(node)
        return False
    
    def getNbors(self,node,graph):
        res = []
        for edge in graph:
            if edge[-1] == node: 
                res.append(edge[0])
        #print(f"node = {node}")
        #print(f"nbors = {res}")
        return res