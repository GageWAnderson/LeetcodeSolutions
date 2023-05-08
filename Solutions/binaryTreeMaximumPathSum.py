# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # Can be modified from within recursive function
        # Has to do with how Python manages variable scope

        def dfs(root):
            if not root:
                return 0
            
            # Typical pattern for tree problems
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Could be negative, so set to 0 if that's true to disculde negatives
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute the max path sum with split from root node
            # Unsplit path goes up to the parent
            # While split path stays in its subtree going through root
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the unsplit path
            # Have to choose either left or right and include the root
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]