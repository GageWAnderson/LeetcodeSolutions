from collections import defaultdict, deque
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        levels: dict[int, list[int]] = defaultdict(list)
        if not root:
            return []
        queue: deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))
        while queue:
            curr_node, curr_level = queue.popleft()
            levels[curr_level].append(curr_node.val)
            if curr_node.left:
                queue.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_level + 1))

        ans: list[list[int]] = []
        for level in levels.items():
            ans.append(level[1])
        return ans
