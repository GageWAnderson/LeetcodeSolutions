#Least common ancestor, solved in O(n) through find,follow, and common helper functions

def find(T,node):
    val = node.val
    if(T.val == val):
        return []
    elif(not T.left and not T.right):
        return None
    else:
        left = find(T.left,node)
        if left:
            return [0] + left
        right = find(T.right,node)
        if right:
            return [1] + right
        return None

def LCA(T,a,b):
    aPath = find(T,A) #O(n)
    bPath = find(T,b)

    if aPath and bPath:
        return follow(commonPrefix(aPath,bPath))
        #O(n) if tree is unbalanced
        #O(log(n)) if tree is balanced
    else:
        return None