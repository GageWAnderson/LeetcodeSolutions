# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # Postorder traversal to reverse/delete
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left,root.right = root.right,root.left
            return root