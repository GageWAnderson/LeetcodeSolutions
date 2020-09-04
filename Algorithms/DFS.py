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

    def dfs_backtracking(self,graph,n,used,depth_limit,depth,curr,ans):
        '''
        Implement permutation of k items out  of n items
        depth: start from 0, and represent the depth of the search
        used: track what items are  in the partial solution from the set of n
        curr: the current partial solution
        ans: collect all the valide solutions
        '''

        if depth == depth_limit: #end condition
        ans.append(curr[::]) # use deepcopy because curr is tracking all partial solution, it eventually become []
        return
    
        for i in range(n):
            if not used[i]:
            # generate the next solution from curr
            curr.append(a[i])
            used[i] = True

            # move to the next solution
            dfs_backtracking(self,graph,n,used,depth_limit,depth+1,curr,ans)
            
            #backtrack to previous partial state
            curr.pop()
            used[i] = False
        return
    # Called as dfs_backtracking(a, n, n, 0, used, [], ans)

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
    
