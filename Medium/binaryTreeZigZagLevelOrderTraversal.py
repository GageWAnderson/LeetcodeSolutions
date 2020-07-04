# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        #Level-order = BFS (use a queue)
        #In-order = DFS (use recursion)
        level = 0
        res = []
        if not root: 
            return res
        res.append([])
        Q = [] #Use the python syntax for fast tail-removal eventually
        #Don't need to mark as seen since this is a tree not a graph

        Q.append((root,level)) #Keep track of level with the node in a tuple
        while len(Q) > 0:
            (v,level) = Q.pop(0)
            if len(res) <= level:
                res.append([])
            if level % 2 == 0: #Level is even, go left
                res[level].append(v.val)
            else: #Level is odd, go right
                res[level].insert(0,v.val)
            
            if v.left:
                Q.append((v.left,level+1))
            if v.right:
                Q.append((v.right,level+1))
        return res
        
        

                #I literally just read that I need to be able to do this algo with my eyes closed...
#         1  procedure BFS(Graph,source):
# 2      create a queue Q
# 3      enqueue source onto Q
# 4      mark source
# 5      while Q is not empty:
# 6          dequeue an item from Q into v
# 7          for each edge e incident on v in Graph:
# 8              let w be the other end of e
# 9              if w is not marked:
# 10                 mark w
# 11                 enqueue w onto Q

#There is definitely a better way of doing this than tracking levels in a tuple...

#Can also use regular BFS with post-processing
#This is a good brute-force solution
        # for i in range(len(result)):
        #     if i % 2 == 1:
        #         result[i] = result[i][::-1]
        # return result