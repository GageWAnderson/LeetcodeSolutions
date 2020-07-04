# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        resStack = []
        stack = []
        
        stack.append(root)
        while len(stack) > 0:
            v = stack.pop()
            resStack.append(v.val)
            
            if v.left:
                stack.append(v.left)
            if v.right:
                stack.append(v.right)
                
        #result is simply the reverse of the resStack built up
        resStack.reverse()
        return resStack
    
#Recursive solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
        
#         def helper(node):
#             if not node:
#                 return
#             else:
#                 helper(node.left)
#                 helper(node.right)
#                 res.append(node.val)
        
#         helper(root)
#         return res