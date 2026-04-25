#Topological Sort provides a linear ordering of verticies such that:
#For every directed edge uv, u comes before v in the ordering
#Note, Topsort only works for DAGs

from collections import defaultdict
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.append(v)
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) #Pass stack in as a variable to modify in call

        return reversed(stack) # Literally DFS, but return in the opposite of order visited

def has_cycle(graph):
    """
    Keep track of the nodes currently in the call stack.
    If you visit a node currently in the call stack you have a cycle in the graph.
    """
    visited = set()
    rec_stack = set()
    
    def has_cycle_helper(node):
        if node in rec_stack:
            return True # Back-Edge Detected, Directed Graph has a cycle
        visited.add(node)
        rec_stack.add(node)
        for nbor in graph[node]:
            if nbor not in visited:
                if has_cycle_helper(nbor):
                    return True
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if has_cycle_helper(node):
            return True
    return False

def topological_sort(graph):
    if has_cycle(graph):
        return None
    
    dfs_visited_order = []
    visited = set()

    def topsort_helper(n):
        visited.add(n)
        for nbor in graph[n]:
            if nbor not in visited:
                topsort_helper(nbor)
        dfs_visited_order.append(n)

    for node in graph:
        if node not in visited:
            topsort_helper(node)

    return list(reversed(dfs_visited_order))

import random
from collections import defaultdict
if __name__ == "__main__":
    num_nodes = 100
    num_nbors_low = 0
    num_nbors_high = 10
    graph = defaultdict(list)
    for i in range(num_nodes):
        num_nbors = random.randint(num_nbors_low, num_nbors_high)
        graph[i] = random.sample(range(num_nodes), num_nbors)
    
    print(topological_sort(graph))