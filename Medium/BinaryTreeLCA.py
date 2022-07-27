class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root, p, q):
        
        def postorder(node):
            if not node:
                return False
            else:
                left = postorder(node.left)
                right = postorder(node.right)
                mid = node == p or node == q
                
                if mid + left + right >= 2:
                    self.ans = node
                
                return mid or left or right
        
        postorder(root)
        return self.ans
        
        