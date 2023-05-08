class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

class MySolution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        prehead = ListNode(-1)
        p1,p2 = l1,l2
        res = prehead
        while p1 and p2:
            if p1.val <= p2.val:
                res.next = p1
                p1 = p1.next
            else:
                res.next = p2
                p2 = p2.next
            res = res.next
        
        res.next = p1 if p1 is not None else p2
        return prehead.next