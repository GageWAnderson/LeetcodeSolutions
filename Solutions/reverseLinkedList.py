# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        prevNode = None
        currNode = head
        nextNode = head.next

        while currNode:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            if nextNode:
                nextNode = currNode.next
        
        return prevNode