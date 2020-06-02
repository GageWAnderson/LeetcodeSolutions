"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    #NOTE: This method is destructive, they never said you couln't do that
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        copy = Node(head.val,None,None)
        copyCurr = copy
        prev,curr = head,head.next
        randoms = [head.random]
        
        while curr is not None:
            prev.next = copyCurr
            randoms.append(curr.random)
            new = Node(curr.val,None,None)
            copyCurr.next = new
            copyCurr = new
            prev = curr
            curr = curr.next
        prev.next = copyCurr #Last element
        
        copyCurr = copy
        for randomP in randoms:
            if not randomP:
                copyCurr.random = None
            else:
                copyCurr.random = randomP.next
            copyCurr = copyCurr.next
            
        return copy
        
#COMPILED,RAN,WITH THE RIGHT ANSWER RIGHT OFF THE PAPER!!! :)

#Very careful testing of 2 edge cases
#Careful walkthrough of larger (4 nodes) test case with both back/front random pointers
#This last test caught that prev.next was not set for the last node

#Key insight was to modify the next in the copied linked list to point to their originals
#So that the originals can still be accessed for their random pointers

#Issues:
#Was mixing up prev,curr
#Need more whitespace in loops when writing out code on paper/whiteboard, otherwise
#I end up having to erase

#This was the complex solution in O(n) time and O(n) space (needed a vector to store the random pointers)
#However, a 1-pass solution is possible in O(n) space if a hash map is used 

#ALTERNATE: Can view this as a graph search problem, since the L.L is actually a graph now! (DFS/BFS implementation is now possible!)