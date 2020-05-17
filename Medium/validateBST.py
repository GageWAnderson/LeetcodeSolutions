# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Had to look at solution to get an elegant way to constrain the value for each of the nodes... (use upper/lower bounds!!!)
class Solution:
    def traverseTree(self, root: TreeNode, lower: int, upper: int) -> bool: #Keep track of upper, lower limits and compare values to thosse instead of the parents!
        #All values must be greater than lower, less than upper
        print(f"upper = {upper}, lower = {lower}")
        if not root: return True #Is NULL
        elif not root.left and not root.right and root.val > lower and root.val < upper: return True #Is leaf, issue was that I wasn't checking the leaves...
        elif not root.right:
            return root.val > lower and root.val < upper and self.traverseTree(root.left,lower,root.val)
        elif not root.left:
            return root.val > lower and root.val < upper and self.traverseTree(root.right,root.val,upper)
        else:
            return root.val > lower and root.val < upper and self.traverseTree(root.left,lower,root.val) and self.traverseTree(root.right,root.val,upper)
        
    def isValidBST(self, root: TreeNode) -> bool: #DUPLICATES ARE NOT ALLOWED, READ THE QUESTION
        lower = -2**31 - 1 #intMin - 1
        upper = 2**31 #intMax + 1, seems like leetCode is only working with 32-bit integers here...
        return self.traverseTree(root,lower,upper)