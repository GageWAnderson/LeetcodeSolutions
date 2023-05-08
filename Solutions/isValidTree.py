from collections import defaultdict

"""
Had the exact correct approach, stumbled on the implementation.
Will get easier as I do more DFS problems.
"""
class Solution:

    def makeAdjacencyList(self, edges):
        res = defaultdict(list)
        for edge in edges:
            res[edge[0]].append(edge[1])
            res[edge[1]].append(edge[0]) # Undirected Graph
        print(res)
        return res

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        
        graph = self.makeAdjacencyList(edges)
        seenNodes = set()
        # recursionStack = [] # Can track Parent to save space

        def getNbors(node):
            return graph[node]
        
        def detectCycle(node, parent): # Just need to track parent, don't need to use recursion stack
            seenNodes.add(node)
            for nbor in getNbors(node):
                if nbor == parent:
                    continue
                if nbor in seenNodes:
                    return True
                elif detectCycle(nbor, node):
                    return True
            return False
        
        hasCycle = detectCycle(0, -1)
        if hasCycle:
            return False
        elif len(seenNodes) < n:
            return False # Tree must be fully connected
        else:
            return True