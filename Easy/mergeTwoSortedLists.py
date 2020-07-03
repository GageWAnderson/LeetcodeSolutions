# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: #This will loop forever if given circular linked lists, use tortoise-hare to check
        if l1 is None and l2 is None: return None #clean up the input
        elif l1 is None: return l2
        elif l2 is None: return l1
        else:
            startNodes = [l1,l2]
            p1 = min([l1,l2], key = lambda node: node.val if node else None) #p1,p2 starting in the same place caused a nasty bug where a cycle was generated
            startNodes.remove(p1)
            p2 = startNodes[0]
            res = p1
            curr = p1
            p1 = p1.next
            while p1 is not None and p2 is not None:
                print(f"p1 = {p1}, p2 = {p2}")
                if(p1.val < p2.val):
                    curr.next = p1
                    p1 = p1.next
                    curr = curr.next
                else:
                    curr.next = p2
                    p2 = p2.next
                    curr = curr.next
            while p1 is not None: #If some of p1 remains after getting to the end of p2
                print(f"p1 = {p1}, p2 = {p2}")
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            while p2 is not None: #If some of p2 remains after getting to the end of p1
                print(f"p1 = {p1}, p2 = {p2}")
                curr.next = p2
                p2 = p2.next
                curr = curr.next
            
            return res