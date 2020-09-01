from collections import defaultdict
class DFS:
    def dfs_recursive(self,graph : Graph ,start : int) -> None: #O(V + E)
        seen = set()

        def dfs(v,seen):
            seen.add(v)
            print(v)
            for nbor in graph.get_nbors(v):
                if nbor not in visited:
                    dfs(nbor,seen)

        dfs(start,seen)
    
    def dfs_iterative(self,graph,start):
        stack = []
        stack.append(start)
        seen = set()

        while stack:
            currNode = stack.pop()
            print(currNode)
            if currNode not in seen:
                seen.add(currNode)
                for nbor in graph.get_nbors(currNode):
                    if nbor not in seen:
                        stack.append(nbor)

class Graph: #Adjacency List
    def __init__(self,verticies : List[int], edges : List[(int,int)]) -> None:
        self.verts = {vertex:[] for vertex in verticies}
        for edge in edges:
            self.verts[edge[0]].append(edge)
    
    def get_nbors(self,vertex : int):
        if vertex in self.verticies.keys():
            return self.verticies[vertex]
        else:
            raise KeyError("Vertex not in graph.")
    
