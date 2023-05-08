# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:], inorder[:mid])
        # preorder[mid + 1] is the root of the right subtree, that's the insight I missed
        # otherwise, I had the rest of the approach
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionHashTable:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorderIndicies = dict() # O(n) pre-work for O(1) lookup time at each step
        for i,node in enumerate(inorder):
            inorderIndicies[node] = i

        def build(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorderIndicies[preorder[0]]
            root.left = self.buildTree(preorder[1:], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
            return root
        
        return build(preorder, inorder)