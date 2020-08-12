# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

#Level-order traversal = BFS
#My hacky first solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return [] #Forgot to account for this edge-case
        queue = deque()
        ans = []
        thisLevel = []
        level = 0
        queue.append((root,level))
        while queue:
            node = queue.popleft()
            currNode,currLevel = node[0],node[1]
            print(f"node = {currNode.val}, currLevel = {currLevel}, level = {level}")
            if currLevel != level:
                ans.append(thisLevel)
                thisLevel = []
                level += 1
            thisLevel.append(currNode.val)
            if currNode.left:
                queue.append((currNode.left,level+1))
            if currNode.right:
                queue.append((currNode.right,level+1))
        ans.append(thisLevel)
        return ans

#Elegant, re-usable python from the answers
class SolutionElegant:
    def levelOrder(self,root):
        if not root: return root

        queue = deque() #Use collections.deque for constant-time popleft operation
        queue.append(root)
        res = []

        while queue:
            level = []
            levelSize = len(queue)
            while levelSize != 0: #Use this to avoid a tuple for storing the level of a point
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                levelSize -= 1
            res.append(level)
        
        return res

class SolutionBetter:    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        layer = [root]
        ans = []
        while layer:
            newlayer = []
            layervals = []
            for node in layer:
                layervals.append(node.val)
                if node.left: newlayer.append(node.left)
                if node.right: newlayer.append(node.right)
            ans.append(layervals)
            layer = newlayer
        return ans