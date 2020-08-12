# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Hold on, so the preorder/inorder traversals don't have enough information to construct the tree?
#Yes, since you don't know where the NULL nodes are located...

#Need to get the preorder traversal of both sides (knowing the inorder traversal for right/left sides)
  #Can only think of doing this through a set...
    
#O(nlogn) work
#Indexing method works for preorder, so I don't need to use a set
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        root = TreeNode(preorder[0]) #root.left, root.right are initially None
        splitIndex = inorder.index(preorder[0])
                
        leftInorder = inorder[:splitIndex]
        rightInorder = inorder[splitIndex+1:] if splitIndex < len(inorder) else []
        leftPreorder, rightPreorder = preorder[1:splitIndex+1],preorder[splitIndex+1:]
        
        #Key insight: preorder left is between the beginning and root index
        #Preorder right is preorder after the root index (makes send visually)
        
        root.left = self.buildTree(leftPreorder,leftInorder)
        root.right = self.buildTree(rightPreorder,rightInorder)
        
        return root