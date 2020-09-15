# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Need to sort each col by row
#O(nlogn) solution
from collections import defaultdict
from functools import cmp_to_key
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        nodeDict = defaultdict(list)
        
        def compare(p1,p2): #Don't factor vals into the sort
            row1,val1 = p1 #Just do it in-place with .sort()
            row2,val2 = p2
            
            if row1 < row2:
                return -1
            elif row1 > row2:
                return 1
            else:
                return 0
        
        
        def inorder(node,row,col):
            if not node:
                return
            else:
                nodeDict[col].append((row,node.val))
                inorder(node.left,row+1,col-1)
                inorder(node.right,row+1,col+1)
                return
        
        inorder(root,0,0) #O(n)
        cols = list(nodeDict.keys())
        cols.sort() #O(nlogn), in-place
        for col in cols:
            nodeDict[col].sort(key = cmp_to_key(compare))
        return [[node[1] for node in nodeDict[col]] for col in cols] #O(n)