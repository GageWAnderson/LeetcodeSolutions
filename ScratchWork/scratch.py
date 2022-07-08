class Node:
    def __init__(self, i):
        self.val = i
        self.edges = []

    def __repr__(self):
        return "Node: val = "+str(self.val)+" edges="+str(self.edges)

class UndirectedGraph:
    """
    Edges are a list of (node1, node2, dist) tuples.
    n is the number of verticies enumerated from 0 to n-1.
    """
    def __init__(self, n, edges):
        # Assumes verticies are numbered from 0 to n-1
        self.graph = [Node(i) for i in range(0, n)]
        for edge in edges:
            (n1, n2, d) = edge
            self.graph[n1].edges.append(Node(n2))
            self.graph[n2].edges.append(Node(n1))

    def __repr__(self) -> str:
        return str([str(node) for node in self.graph])

class KeyAlgorithms:
    def bfs(graph):
        """
        Traverses a graph with bfs, returns nothing.
        Uses imperative method using a queue.
        """
        from collections import deque
        q = deque()
        seen = set()
        q.append(graph[0]) 
        while q:
            currNode = q.popleft()
            print(currNode)
            for nbor in currNode.edges:
                if nbor not in seen:
                    q.append(nbor)
                    seen.add(nbor)

    def dfs(graph):
        seen = set()
        def dfs_helper(seen_set, node):
            if node not in seen_set:
                print(node)
                seen_set.add(node)
                for nbor in node.edges:
                    dfs_helper(seen_set,nbor)
        dfs_helper(seen,graph[0])

    def binary_search(x,A):
        if len(A) == 0:
            return -1
        
        l,h = 0,len(A)-1
        while l <= h:
            mid = l + (h - l) // 2
            if A[mid] == x:
                return mid
            elif A[mid] < x:
                l = mid+1
            else:
                h = mid-1
        return -1
        
    if __name__ == "__main__":
        edges = [(0,1,3),(0,2,5),(2,3,1),(1,3,2)]
        g = UndirectedGraph(4,edges)
        print("running bfs")
        bfs(g.graph)
        print("running dfs")
        dfs(g.graph)

# Got all of these correct, but somewhat inefficient on the first try
# Seems like you still remember the basics!