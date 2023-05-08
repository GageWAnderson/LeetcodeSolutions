# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        prev = None
        while curr:
            size += 1
            prev = curr
            curr = curr.next
        
        target = size - n + 1
        count = 1
        curr = head
        prev = None
        while curr:
            if count == target:
                if prev:
                    prev.next = curr.next
                    return head
                else:
                    return curr.next
            
            prev = curr
            curr = curr.next
            count += 1
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionOptimal:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remember the paradigms of dummy nodes at the head and tail
        and fast/slow pointer.
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            # Keep a constant distance of n between left and right
            # Therefore, you know how many nodes you are from the end
            left = left.next
            right = right.next
        
        #delete the node
        left.next = left.next.next
        return dummy.next # Dummy Accounts for possibility of removing the head