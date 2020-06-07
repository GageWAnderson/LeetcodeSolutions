#Use modified merge sort in-place with Linked lists.

#Made a minor mistake in merge that missed the last recursive merge
#Best to have the main function be the clean mergesort-mergesort-merge model

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Should get the length here in 1 pass with a slow,fast pointer (faster by a const. factor)
    def splitAtMid(self,A):
        Llen = 0
        p = A
        while p:
            Llen += 1
            p = p.next
        #print(f"Llen = {Llen}")
        
        i,p = 1,A
        while(i < Llen//2): #i must be 1 to properly break out the list
            p = p.next
            i += 1
        mid = p.next
        p.next = None
        return mid
    
    def merge(self,left, right): 
        dummy = curr = ListNode()

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        elif right:
            curr.next = right

        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if(head and head.next): #I got the first part (splitting) right on the first try
            R = self.splitAtMid(head)
            L = head
            
            L = self.sortList(L)
            R = self.sortList(R)
            #print(f"L = {L}, R= {R}")
            
            
            #Merge the linked lists pL and pR together
            #With interleaving
            return self.merge(L,R)
            
        return head #Need an outer return case to account for edge case where input is of size 1