# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        currNode = head,
        currNode = currNode[0]
        prevNode = None
        prevPrevNode = None
        counter = 1
        while currNode:
            if counter % 2 == 0:
                if counter == 2:
                    head = currNode
                else:
                    prevPrevNode.next = currNode
                prevNode.next = currNode.next
                currNode.next = prevNode
                prevPrevNode = currNode
                currNode = prevNode.next
            else:
                prevPrevNode = prevNode
                prevNode = currNode
                currNode = currNode.next
            counter += 1
        return head