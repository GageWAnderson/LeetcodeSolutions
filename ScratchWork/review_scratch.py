def dfs(start, graph):
    seen = set()

    def visit(n):
        print(n)
    
    def get_nbors(g, n):
        return g[n] # Assumes graph is an adjacency list

    def dfs_helper(node):
        seen.add(node)
        visit(node)
        for nbor in get_nbors(graph, node):
            if node not in seen:
                dfs_helper(nbor)
    
    dfs_helper(start)

from collections import deque
def bfs(start, graph): # Also handles level-order traversal of a Binary Tree
    queue = deque()
    seen = set()

    def visit(n):
        print(n)
    
    def get_nbors(g, n):
        return g[n]

    queue.append(start)
    while queue:
        curr_node = queue.popleft()
        visit(curr_node)
        seen.add(curr_node)
        for nbor in get_nbors(graph, curr_node):
            if nbor not in seen:
                queue.append(nbor)

def inorder_traveral(start_node):
    res = []

    def inorder_helper(node):
        if not node:
            return
        inorder_helper(node.left)
        res.append(node.val)
        inorder_helper(node.right)
    
    inorder_helper(start_node)
    return res

def preorder_traversal(start_node):
    res = []

    def preorder_helper(node):
        if not node:
            return
        res.append(node.val)
        preorder_helper(node.left)
        preorder_helper(node.right)
    
    preorder_helper(start_node)
    return res

def postorder_traversal(start_node):
    res = []

    def postorder_helper(node):
        if not node:
            return
        postorder_helper(node.left)
        postorder_helper(node.right)
        res.append(node.val)
    
    postorder_helper(start_node)
    return res

def binary_search(arr, x): # Only works on sorted arrays
    start,end = 0,len(arr) - 1

    while start <= end:
        mid = (end + start) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return None

# Has Cycles --> Determine if a graph is a DAG
def has_cycles(graph):
    return False # TODO: Implement DFS Cycle detection

# Topological Sort
def topological_sort(graph):
    if has_cycles(graph):
        return None
    
    res = []
    seen = set()

    def get_nbors(node):
        return graph[node]

    def dfs(node):
        res.append(node)
        seen.add(node)
        for nbor in get_nbors(node):
            if nbor not in seen:
                dfs(nbor)
    
    # Account for disconnected graphs and the possiblility that start isn't the first node in the topsort?

class TrieNode:

    def __init__(self):
        self.isEndOfWord = False
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        currNode = self.root
        last_word_index = len(word) - 1

        for i,letter in enumerate(word):
            if letter not in currNode.children:
                new_node = TrieNode()
                currNode.children[letter] = new_node
            currNode = currNode.children[letter]
            if i == last_word_index:
                currNode.isEndOfWord = True
    
    def contains(self, word):
        currNode = self.root

        for letter in word:
            if letter not in currNode.children:
                return False
            currNode = currNode.children[letter]
        
        if not currNode.isEndOfWord:
            return False
        
        return True
    
    def starts_with(self, word):
        currNode = self.root

        for letter in word:
            if letter not in currNode.children:
                return False
            currNode = currNode.children[letter]
        
        return True


def mergesort(arr):

    def merge(arr1, arr2):
        res = []
        i,j = 0,0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        
        return res # O(n + m) time and memory
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def quicksort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr


class UnionFind:

    def __init__(self, n): # Nodes from 0 to n-1
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]
    
    def __str__(self):
        return f"parents = {self.parents}, ranks = {self.ranks}"
    
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)
        if self.parents[p1] == self.parents[p2]:
            return 0 # No Union Performed
        
        if self.ranks[p2] > self.ranks[p1]:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        else:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        
        return 1
    
    def find(self, n1):
        res = n1

        while res != self.parents[res]:
            self.parents[res] = self.parents[self.parents[res]] # Path Compression
            res = self.parents[res]
        
        return res


import random
if __name__ == "__main__":
    uf = UnionFind(100)

    res = 0
    for i in range(1, 100):
        res += uf.union(i-1, i)
    
    print(uf)
    print(f"number of connected components = {100 - res}")