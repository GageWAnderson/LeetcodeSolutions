# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return [] #Keep forgetting this
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            l = len(queue)
            level = []
            
            while l > 0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    level.append
                l -= 1
            res.append(level)
        return reversed(res)