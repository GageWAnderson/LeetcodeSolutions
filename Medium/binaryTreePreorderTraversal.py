# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [] 
        #Use BFS, but with a stack to do iterative DFS
        stack.append(root)
        while len(stack) > 0:
            v = stack.pop()
            res.append(v.val)
            
            if v.right: #Need to reverse right,left when doing iterative DFS
                stack.append(v.right)
            if v.left:
                stack.append(v.left)
        
        return res
                
        
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         def helper(node):
#             if node:
#                 res.append(node.val)
#                 helper(node.left)
#                 helper(node.right)
        
#         helper(root)
#         return res