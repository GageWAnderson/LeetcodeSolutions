from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        seen = set()

        def dfs(node):
            seen.add(node)
            for nbor in graph[node]:
                if nbor not in seen:
                    dfs(nbor)
        
        numConnected = 0
        for node in range(n):
            if node not in seen:
                numConnected += 1
                dfs(node)
        
        return numConnected


from collections import defaultdict
class SolutionUnionFind:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != parent[res]: # Representative nodes at root are their own parent
                parent[res] = parent[parent[res]] # Path compression optimization
                res = parent[res]
            
            return res
        
        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            # Nodes are in the same connected component
            if parent1 == parent2:
                return 0
            
            # Nodes are in different connected components
            # Merge the smaller connected component into the larger one
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            return 1
        
        numConnectedComponents = n
        for n1, n2 in edges:
            # Reduce the number of connected components when merging
            numConnectedComponents -= union(n1, n2)
        return numConnectedComponents