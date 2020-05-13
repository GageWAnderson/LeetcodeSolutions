# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution1:
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

    # Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        L = ListNode(0,None)
        L1Ended = False
        L2Ended = False
        curr1 = l1
        curr2 = l2
        curr3 = L
        sum = 0
        while((not L1Ended) or (not L2Ended)):                        
            if(L1Ended): 
                val1 = 0
            else:
                val1 = curr1.val
            if(L2Ended): 
                val2 = 0
            else:
                val2 = curr2.val
            
            if(not L1Ended):
                curr1 = curr1.next
                if(curr1 is None): 
                    L1Ended = True
            if(not L2Ended):
                curr2 = curr2.next
                if(curr2 is None):
                    L2Ended = True
            
            sum = val1 + val2 + sum
            rem = sum % 10
            quot = sum // 10
            sum = quot
            print(f"sum = {sum}")
            curr3.val = rem
            print(f"curr3.val = {curr3.val}")
            curr3.next = ListNode(quot,None)
            if(L1Ended and L2Ended and sum == 0):
                curr3.next = None
                break
            curr3 = curr3.next
        
        return L