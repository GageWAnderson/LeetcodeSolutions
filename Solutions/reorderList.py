# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(n) memory isn't optimal, can go faster with a 2-pointers approach
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Missed the fast/slow pointers paradigm for Linked List algorithms.
        For example, the tortoise/hare alorithm for linked list cycle detection.
        """
        backPointers = dict()
        n = 0

        prev = None
        curr = head

        while curr:
            backPointers[curr] = prev
            prev = curr
            curr = curr.next
            n += 1
        
        tail = prev
        count = 0
        p1, p2 = head, tail

        while p1 != p2 and count < (n - 1) // 2:
            tmp = p1.next
            p1.next = p2
            p1 = tmp

            p2.next = p1
            p2 = backPointers[p2]

            count += 1
        
        if p1 == p2:
            p1.next = None
        else:
            p2.next = None
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionOptimal:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Use Fast and Slow pointer to find middle of list. Remember the fast/slow pointer paradigm
        for future linked-list problems.
        """
        # Find Middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Slow is now the middle
        # Reverse the 2nd half of the linked list
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Prev is now the tail element
        p1,p2 = head,prev
        while p2.next:
            tmp = p1.next
            p1.next = p2
            p1 = tmp

            tmp = p2.next
            p2.next = p1
            p2 = tmp