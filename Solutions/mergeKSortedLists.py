# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from functools import cmp_to_key
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def compareListNodes(n1, n2):
            if n1.val < n2.val:
                return -1
            elif n1.val == n2.val:
                return 0
            else:
                return 1
        
        dummy = ListNode(-1)
        key_func = cmp_to_key(compareListNodes)
        tail = dummy
        headPointers = []

        for i in range(len(lists)): # Initialize the pointers
            if lists[i] is not None:
                heapq.heappush(headPointers, key_func(lists[i]))

        while len(headPointers) > 0:
            minPointer = heapq.heappop(headPointers).obj
            tail.next = minPointer
            tail = tail.next
            nextNode = minPointer.next
            if nextNode is not None:
                heapq.heappush(headPointers, key_func(nextNode))
        
        return dummy.next