# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(log(n) + k), O(log(n)) space (recursion stack)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        numNodesTraversed = [0]
        def getTreeSize(node):
            if not node:
                return 0
            else:
                return 1 + getTreeSize(node.left) + getTreeSize(node.right)
        
        def inOrderTraversal(node):
            if res[0] is not None:
                return
            elif not node:
                return
            
            inOrderTraversal(node.left)

            numNodesTraversed[0] += 1
            if numNodesTraversed[0] == k:
                res[0] = node.val
                return

            inOrderTraversal(node.right)

            return

        
        inOrderTraversal(root)
        return res[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionIterative:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while True:
            while cur: # Add left nodes to stack
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right # Repeat for the right node if not found

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = [0]

        def inorder_traversal(node):
            if not node:
                return None
            
            left = inorder_traversal(node.left)
            if left is not None:
                return left
            n[0] += 1
            if n[0] == k:
                return node.val
            return inorder_traversal(node.right)
        
        return inorder_traversal(root)