# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverse(self, L: ListNode):
        prev = None
        next = None
        curr = L
        while(not (curr.next is None)):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev #keep forgetting this line, need to set the pointer for the last list node
        return curr
    
    def readList(self, L: ListNode):
        x = 0
        curr = L
        while((curr is not None)):
            x *= 10
            x += curr.val
            curr = curr.next
        return x
    
    def makeList(self, x: int):
        L = ListNode(0,None)
        curr = L
        while(x != 0):
            z = x%10
            x = x//10
            curr.val = z
            if(x == 0):
                break
            next = ListNode(0,None)
            print(f"z = {z}")
            curr.next = next
            curr = next
        return L
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        L1_r = self.reverse(l1)
        L2_r = self.reverse(l2)
        x = self.readList(L1_r)
        y = self.readList(L2_r)
        sum = x + y
        return self.makeList(sum)
        

        
    #Remember to write self. when calling helper functions in classes
    #Read the problem statement carefully, you were returning the wrong thing, needed to return a linked list
    
    #Handling the default objects that LeetCode gives you is a little confusing...