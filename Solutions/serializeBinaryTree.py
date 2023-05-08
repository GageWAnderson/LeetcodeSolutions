# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Pre-Order Traversal with a String Builder -> String Conversion
    def serialize(self, root):
        """Encodes a tree to a single string.

        Over-thought the answer. I was trying to do Pre-Order traversal without
        having to include Null in the answer -> definitely saves space.
        
        :type root: TreeNode
        :rtype: str
        """
        res = [] # Got String builder data structure right (key paradigm to remember)

        def dfs(node): # Pre-Order Traversal
            if not node:
                res.append("n")
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return ",".join(res) # Turn String Builder into a String
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "n":
                self.i += 1
                return None
            else:
                node = TreeNode(int(vals[self.i]))
                self.i += 1
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))