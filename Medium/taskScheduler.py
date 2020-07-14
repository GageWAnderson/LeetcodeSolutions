#Inefficient Attempt (Didn't use a priority Queue)
from collections import deque
class Solution:
    def linSearch(self,inQ,inst):
        for elem in inst:
            if elem not in inQ:
                inst.remove(elem)
                return elem
        return "idle"
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if(len(tasks) == 0): return 0 #Clean up the input
        
        res = 0
        inQ = set()
        Q = deque() #This is how you make queues fast in python
        
        while(len(tasks) > 0):
            elem = self.linSearch(inQ,tasks)
            Q.append(elem)
            res += 1
            
            if elem != "idle":
                inQ.add(elem)
            
            if(len(Q) > n):
                oldFront = Q.popleft()
                if oldFront != "idle":
                    inQ.remove(oldFront) 
                    #set.remove() needs to remove something that is already in the set
        
        return res
    
#See high-performance collections for documentation: 
#https://docs.python.org/2/library/collections.html#collections.deque

#Note on how to use collections.deque: use the deque ("deck" or double-ended queue) object
#Allows for O(1) popleft operation

#This attempt was mostly wrong,should use a priority queue method