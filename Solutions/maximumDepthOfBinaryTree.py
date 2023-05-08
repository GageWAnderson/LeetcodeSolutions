# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [1]

        def inOrderTraversal(node, depth):
            if not node:
                return

            res[0] = max(res[0], depth)
            inOrderTraversal(node.left, depth + 1)
            inOrderTraversal(node.right, depth + 1)
            
        inOrderTraversal(root, 1)
        return res[0]   