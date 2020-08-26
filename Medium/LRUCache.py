#Most recent should be a queue to track most recent
#Queue entries should contain pointers to delete what's in the cache when removed from queue
#O(1) removal time, need to track queue capacity and remove elements accordingly

#Is there a data structure that tracks order of use and has O(1) removal time?
#I think so, it is called OrderedDict in python - This solution is a cop-out
class LRUCache:
    def __init__(self, capacity: int):
        self.inCache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        item = self.inCache.get(key, None)
        if not item: return -1
        self.inCache.move_to_end(key)
        return item

    def put(self, key: int, value: int) -> None:
        self.inCache[key] = value
        if len(self.inCache) > self.capacity:
            self.inCache.popitem(last=False) #Data structure tracks LRU
        self.inCache.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Should Write an actual data structure myself to do this

#This is bad since O(n) operations for get,put due to queue DS
class LRUCache_Bad:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.LRU = deque()
        
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.LRU = self.removeKey(self.LRU,key) #O(n)
            self.LRU.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys() and len(self.LRU) >= self.capacity: #This shouldn't run if key is already in the cache
            lruKey = self.LRU.popleft()
            self.LRU = self.removeKey(self.LRU,lruKey) #O(n)
            self.cache.pop(lruKey)
        self.LRU = self.removeKey(self.LRU,key) #O(n)
        self.cache[key] = value
        self.LRU.append(key)
        
    def removeKey(self,queue,key):
        res = deque()
        for item in queue:
            if item != key:
                res.append(item)
        return res

#_______________________________________Better_Solution_____________________________________________#
#Use a hash Map for constant lookup time, double-linked list to keep track of recency
class Node:
    def __init__(self,prev=None,key=None,val=None,nextVal=None):
        self.prev = prev
        self.key = key
        self.val = val
        self.nextVal = nextVal

class DoubleLinkedList: #Dummy nodes in LLs help with edge cases 
    def __init__(self,head=Node(),tail=Node()):
        self.head = head
        self.tail = tail #Dummy Nodes
        self.head.nextVal = self.tail
        self.tail.prev = self.head
    
    def addToHead(self,node):
        currHead = self.head.nextVal
        self.head.nextVal = node
        node.prev = self.head
        node.nextVal = currHead
        currHead.prev = node
    
    def removeNode(self,node):
        prevNode = node.prev
        nextNode = node.nextVal
        
        node.prev = None
        node.next = None
        
        prevNode.nextVal = nextNode
        nextNode.prev = prevNode
        
    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)
        
    def removeFromTail(self):
        tailNode = self.tail.prev
        self.removeNode(tailNode)
        return tailNode
    
#Actually implements a LinkedHashMap with a dict() and a Double-Linked-List
#Dummy head/tail is effective for preventing edge cases
#Using Ordered Map is a cop-out
class LRUCache_Better_Solution:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict() #Put nodes in as the values
        self.LRU = DoubleLinkedList()
        
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            node = self.cache[key]
            self.LRU.moveToHead(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value #Updates the node
            self.LRU.moveToHead(node)
        else:
            newNode = Node(None,key,value,None)
            self.LRU.addToHead(newNode)
            self.cache[key] = newNode
            self.size += 1
        
        if self.size > self.capacity:
            tailNode = self.LRU.removeFromTail()
            del self.cache[tailNode.key]
            self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)