# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        nodes = self.inorder(root)
        print(nodes)
        root.left = None
        currNode = root
        for node in nodes[1:]:
            currNode.right = TreeNode(node,None,None)
            currNode = currNode.right
    
    def inorder(self,root):
        if not root: return []
        return [root.val] + self.inorder(root.left) + self.inorder(root.right)