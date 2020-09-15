#Use BFS to solve the shortest path problem in an unweighted,
#Undirected Graph -Need to record the parent of a given node
class Node:
    def __init__(self,parent,tree_node):
        self.parent = parent if parent else None
        self.left = tree_node.left if tree_node else None
        self.right = tree_node.right if tree_node else None
        self.val = tree_node.val if tree_node else None
    
    def get_nbors(self):
        nbors = []
        if self.parent:
            nbors.append(self.parent)
        if self.left:
            nbors.append(self.left)
        if self.right:
            nbors.append(self.right)
        return nbors
    
    def is_leaf(self):
        return (not self.left) and (not self.right)
    
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        
        def make_graph(node): #Makes an adj. List
            if not node:
                return
            else:
                if node.val == k:
                    start = node
                graph[node.val] = node.get_nbors()
                left_node = Node(node,node.left)
                right_node = Node(node,node.right)
                make_graph(left_node)
                make_graph(right_node)
                return
        
        graph = dict()
        node_root = Node(None,root)
        start = None
        make_graph(node_root)
        
        seen = set()
        q = deque()
        q.append(start)
        while q:
            curr_node = q.popleft()
            if curr_node.is_leaf():
                return curr_node.val
            seen.add(curr_node.val) #All vals are unique
            for nbor in curr_node.get_nbors():
                if nbor.val not in seen:
                    q.append(nbor)
        return -inf