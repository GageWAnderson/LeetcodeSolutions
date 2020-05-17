# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #This problem is really easy (O(N)), however I'm just getting more used to binary tree questions so I did this
    def __init__(self):
        self.ans = []
        
    def traverseTree(self, root: TreeNode):
        if not root: return
        else:
            self.traverseTree(root.left)
            self.ans.append(root.val) #This line is the key for in-order, it represents the current Node
            self.traverseTree(root.right)
            return
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.traverseTree(root)
        return self.ans