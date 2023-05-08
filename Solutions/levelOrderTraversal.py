# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class SolutionBFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append((root, 0))
        res = defaultdict(list)
        while queue:
            currNode,currLevel = queue.popleft()
            res[currLevel].append(currNode.val)
            if currNode.left:
                queue.append((currNode.left, currLevel + 1))
            if currNode.right:
                queue.append((currNode.right, currLevel + 1))
        
        ans = []
        for key in res.keys():
            ans.append(res[key])
        return ans