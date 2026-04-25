class UnionFind:
    """
    The Union-Find (or Disjoint-Set) data structure is used to efficiently 
    represent a collection of disjoint sets and perform operations such as 
    finding the set to which an element belongs and merging two sets together. 
    It has various applications, including solving connectivity problems, detecting cycles in graphs, 
    and implementing efficient 
    algorithms like Kruskal's algorithm for finding minimum spanning trees.

    The Union-Find data structure is versatile and widely used in 
    various algorithms and applications involving disjoint sets and 
    connected components. Its simplicity, efficiency, and 
    ability to handle large-scale problems make it a 
    fundamental tool in computer science and graph theory.
    """

    def __init__(self, n):
        """
        The __init__ method initializes the data structures for the UnionFind object. 
        It creates an array parent to represent the 
        parent of each element and an array rank to store the rank (or depth) of each tree.
        """
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        """
        The find method finds the root (or representative) of the set to which x belongs. 
        It uses path compression to optimize future lookups by updating the parent of 
        each traversed node directly to the root.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        The union method merges the sets that contain elements x and y by performing a union operation. 
        It first finds the roots of both elements using the find method. If the roots are the same, 
        it means the elements are already in the same set, so no further action is needed. 
        Otherwise, the method compares the ranks of the root nodes and performs a union accordingly. 
        If the ranks are equal, it chooses one root to become the 
        parent of the other and increments the rank of the chosen root.
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

if __name__ == "__main__":
    n = 10  # Number of elements
    uf = UnionFind(n)

    # Assembling connected components in the graph
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)

    print(uf.find(1))  # Output: 0
    print(uf.find(3))  # Output: 2

    uf.union(1, 3)

    print(uf.find(3))  # Output: 0 (since 3 is now connected to 0)
    print(uf.find(5))  # Output: 0 (since 5 is also connected to 0)


class UnionFind:
    """
    Union Find is a forest of Trees
    """
    def __init__(self, n : int, edges: list[list[int]]):
        # Assumes nodes from 0 to n - 1
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,n1):
        res = n1
        
        # When a node is a parent of itself we found the representative
        while res != self.parent[res]:
            # Path Compression Optimization:
            # Set the parent of the current node to its grandparent
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        
        return res

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0 # We didn't perform a Union

        # Perform the Union by Rank of p1, p2
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        return 1 # We did perform the Union

class Solution:

    def number_of_connected_components(n, edges):
        uf = UnionFind(n, edges) # O(e + v) time, O(v) memory
        res = n
        for n1, n2 in edges: # O(e)
            # Union as many edges as possible then return the
            # number connected components
            res -= uf.union(n1, n2)
        return res