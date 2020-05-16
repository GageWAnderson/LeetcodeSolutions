#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#The following commented method is too inefficient :(
# def removeNones(lists: List[ListNode]): #Don't modify the list while looping through it!!!
#     #This way of checking for None is very inefficient, need to change it
#     newList = []
#     for L in lists:
#         if L is not None:
#             newList.append(L)
#     return newList #You don't need this function if you use lambda p : (p,p.val) if p is not None else None

#This can be improved by using a heap for finding the minimum, and creating the result in place for O(1) memory usage!
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        #p.val will crash if it is given a NULL pointer! Need to take these NULL list nodes out of the input...
        (res,curr) = (None,None) #Optimize by making res in place, rather than building it up!
        lists = [p for p in lists if p is not None] #List comprehension to eliminate None!
        
        while len(lists) > 0:
            minP = min(lists, key=lambda x: x.val if x is not None else None)
            if(res is None): 
                res = ListNode(minP.val) #Just for the first iteration
                curr = res
            else:
                nextNode = ListNode(minP.val) #NOTE: You should'nt name your variables next
                curr.next = nextNode
                curr = nextNode
            lists.remove(minP) #Need to run this at the start as well!
            if(minP.next is not None):
                lists.append(minP.next)
        
        return res

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

def makePQ(lists):
    PQ = []
    for node in lists:
        if node:
            heapq.heappush(PQ, (node.val, node))
    return PQ

#Significantly better solution using a min-heap
class SolutionBetter: #Uses a heap for O(Nlog(k)) runtime (O(N)) space since we made a new heap
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        (res,curr) = (None,None)
        PQ = makePQ(lists) #Makes a Priority Queue to store the pointers
        
        while PQ: #while PQ is a syntactic shortcut
            minP = heapq.heappop(PQ)[1]
            if(res is None): 
                res = ListNode(minP.val) #Just for the first iteration
                curr = res
            else:
                nextNode = ListNode(minP.val) #NOTE: You should'nt name your variables next
                curr.next = nextNode
                curr = nextNode
            if(minP.next is not None):
                pqItem = (minP.next.val,minP.next)
                heapq.heappush(PQ, pqItem)
        
        return res


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionBest: #Uses the merge lists one by one method
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        list1 = []
        for i in range(len(lists)):
            while lists[i]:
                list1.append(lists[i].val)
                lists[i] = lists[i].next
        
        if list1:
            x = sorted(list1)
            p = ListNode(x[0])
            q = p

            for i in x[1:]:
                p.next = ListNode(i)
                p = p.next

            return q
        return None