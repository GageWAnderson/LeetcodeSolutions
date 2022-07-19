"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pSeen = set()

        currNode = p
        while currNode:
            pSeen.add(currNode.val)
            currNode = currNode.parent

        currNode = q
        while currNode:
            if currNode.val in pSeen:
                return currNode
            else:
                currNode = currNode.parent

        return None
