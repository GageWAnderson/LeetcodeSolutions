# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Got close with the inorder traversal hint, however missed that p1 = prev, p2 = root
#Keep updating p2 only when p1 is chosen
#This has to do with a process called Morris traversal
class Solution:
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.prev = None
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.findProblems(root) #O(n)
        if self.p1 and self.p2:
            self.p1.val,self.p2.val = self.p2.val,self.p1.val
        
        #Reset class attributes
        self.p1,self.p2,self.prev = None,None,None
    
    #Need to run the whole inorder traversal for some reason
    def findProblems(self,root):
        if not root: return
        self.findProblems(root.left)
        print(root.val)
        if self.prev:
            if self.prev.val > root.val:
                if not self.p1:
                    self.p1 = self.prev
                self.p2 = root
        self.prev = root
        self.findProblems(root.right)