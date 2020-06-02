# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#This one was pretty easy because of the hash set
#Got it right first try, however there are methods
#That use 2 pointers that I should also consider..
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        seen = set()
        p = head
        
        while p:
            if p in seen:
                return p
            
            seen.add(p)
            p = p.next
        
        return None

#Two pointers: Move the head and the slow pointer at the same time
        # # Find the entry node of the cycle
        # while head is not one_step_pointer:
        #     head = head.next
        #     one_step_pointer = one_step_pointer.next