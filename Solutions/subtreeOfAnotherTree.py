# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(treeNode, subTreeNode):
            if treeNode is None and subTreeNode is None:
                return True
            elif treeNode is None and subTreeNode is not None:
                return False
            elif subTreeNode is None and treeNode is not None:
                return False
            
            if treeNode.val != subTreeNode.val:
                return False
            
            return sameTree(treeNode.left, subTreeNode.left) and sameTree(treeNode.right, subTreeNode.right)
        
        def traverseNodes(node):
            if sameTree(node, subRoot):
                return True
            if node.left and traverseNodes(node.left):
                return True
            if node.right and traverseNodes(node.right):
                return True
            return False
        
        return traverseNodes(root)