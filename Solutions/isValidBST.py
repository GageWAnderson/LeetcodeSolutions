# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(n) memory, time can be improved 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def inOrderTraversal(node):
            if not node:
                return
            
            inOrderTraversal(node.left)
            res.append(node.val)
            inOrderTraversal(node.right)
        
        inOrderTraversal(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mostRecentNumber = [float('-inf')] # O(n) memory because of recursion stack 

        # Check inOrderTraversal while running it to see if it's in order
        def inOrderTraversal(node):
            if not node:
                return True
            
            if not inOrderTraversal(node.left):
                return False

            if mostRecentNumber[0] >= node.val:
                return False
            else:
                mostRecentNumber[0] = node.val

            if not inOrderTraversal(node.right):
                return False
            
            return True
        
        return inOrderTraversal(root) # Cut in-order traversal as soon as we know the BST doesn't work