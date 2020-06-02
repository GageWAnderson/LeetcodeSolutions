# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next: return None
        counter = 1
        nCurr,nPrev = None,None
        curr = head
        
        while curr is not None: #This worked better than curr.next is not None
            curr = curr.next
            counter += 1
            
            if nCurr:
                nPrev = nCurr
                nCurr = nCurr.next
            
            if counter > n and not nCurr:
                nCurr = head

        #Could do a much better job having more clean return cases    
        if nPrev:
            nPrev.next = nCurr.next
            return head
        elif nCurr and not nPrev: #curr,nCurr are right next to each other
            head = nCurr.next
            nCurr = None
            return head
        else:
            head = curr.next #Was originally segfaulting here
            return head


