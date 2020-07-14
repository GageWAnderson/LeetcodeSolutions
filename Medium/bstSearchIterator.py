# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #Understood that the answer is the inorder traversal,
    #However, got hung up on the details
    def __init__(self, root: TreeNode):
        self.stack = [] #Replace system stack w/ our own stack to have control over recursion
        self._inorder_left(root) #Starts off at the smallest node
        
    def _inorder_left(self,root): #_private_helper_function
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        if top.right:
            self._inorder_left(top.right)
        return top.val #O(1)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#Solution 1: Flatten the BST into an array (Got it right that this doesn't comply w/ the memory requirement)

#Solution 2: Controlled Recursion (iterative inorder traversal)
  #For a given node root, the next smallest element will always be the leftmost node in the tree
  #Most time is spent maintaining the invariant that the stack top will always have the correct node
  #This is a beautiful solution, just do recursion iteratively
    
  #Iterative simulation of recursion is a common stack problem type