# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # I've done this problem before, so was very easy for me
        def preOrderTraversal(node):
            if not node:
                return None
            
            if (p.val <= node.val and q.val >= node.val) or (p.val >= node.val and q.val <= node.val):
                return node
            elif p.val < node.val and q.val < node.val:
                return preOrderTraversal(node.left) # p,q are both on the right side
            else:
                return preOrderTraversal(node.right)
        
        return preOrderTraversal(root)


class SolutionIterative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur