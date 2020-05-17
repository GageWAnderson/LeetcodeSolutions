# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Not used to LeetCode binary tree problems, I will get faster when I am more aquainted with the patterns...
#NOTE This is not a binary search tree, so you will need to keep track of what you have seen
#I'm pretty bad at these problems as of 05/17/2020, so I will need more extensive study of this DS to improve...
class Solution:
    def __init__(self):
        self.anc = None #anc was being allocated on the stack when traverseTree was outside the class
        #Instead, we will store the answer in a class attribute, so both the helper and the main have access to it
        
    def traverseTree(self,root,p,q):
        if not root: return False #NULL Check
        left = self.traverseTree(root.left,p,q) #Remember to include recursive, memoized arguments in the function calls!
        right = self.traverseTree(root.right,p,q)
        mid = (root == p or root == q) #Using these three boolean flags to track if you have found both if pretty good...
        #I got the idea to use boolean flags, but not in this exact setup...

        #If any of these three flags become true, instantly make the answer true
        if mid + left + right >= 2: self.anc = root
        return mid or left or right
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.traverseTree(root,p,q)
        return self.anc