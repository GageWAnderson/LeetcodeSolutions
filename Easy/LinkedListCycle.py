# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#This one was easy, I already knew the answer
#Answer was clean with no bugs right off the whiteboard-good job!
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow,fast = head,head
        
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                return True
            
        return False